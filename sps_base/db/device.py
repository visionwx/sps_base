from sps_base.collections import COLLECTIONS
from sps_base.exceptions import UserNotExistException, HouseNotExistException, DeviceNotExistException
from google.cloud import firestore
from sps_base.pubsub.publisher import publishDeviceCreateTopic, publishDeviceUpdateTopic, publishDeviceDeleteTopic
from sps_base.db.base import Collection, Document, UserHouseCollection

# 将 dict2 合并 到 dict1, 支持多级嵌套合并
def mergeDict(dic1, dic2):
    for i in dic2:
        if i in dic1:
            if type(dic1[i]) is dict and type(dic2[i]) is dict:
                mergeDict(dic1[i], dic2[i])
        else:
            dic1[i] = dic2[i]

# 将 updateData 解析成 完全的字典格式
# updateData = {
#   "states.online": True,
#   "states.isArmed": False,
# }
def parseUpdateData(updateData):
    result = {}
    for k,v in updateData.items():
        # 提取keys列表
        kList = k.split(".")
        kList.reverse()
        # 从最后一个字段值开始初始化
        vRef = {
            kList[0]: v
        }
        # 往前嵌套字段值
        kListLength = len(kList)
        for i in range(1, kListLength):
            vRef = {
                kList[i]: vRef
            }
        # 合并到result
        mergeDict(result, vRef)
    return result

# 即将废弃
# 把字典格式的 condition 转换成 三元组
def parseCondition(condition):
    if type(condition) is not dict:
        return None,None,None
    for fieldName in condition.keys():
        for op,fieldValue in condition[fieldName].items():
            return fieldName,op,fieldValue
    return None,None,None

# 设备 文档类
class DeviceDocument(Document):
    # 构造函数，重写
    def __init__(self, userId, houseId, deviceId):
        self.userId = userId
        self.houseId = houseId
        self.deviceId = deviceId
        self.REF = self.getDocumentRef()
        
    # 获取设备数据库引用
    def getDocumentRef(self):
        # 检查用户，房子，是否存在
        deviceRef = self.DB.collection(COLLECTIONS.users
            ).document(self.userId
            ).collection(COLLECTIONS.houses
            ).document(self.houseId
            ).collection(COLLECTIONS.devices
            ).document(self.deviceId)
        return deviceRef
    
    # 数据创建接口 重写
    def create(self, data):
        # 数据检查
        # 执行操作
        result = super().create(data)
        # 发布事件
        publishDeviceCreateTopic(
            self.userId, 
            self.houseId, 
            self.deviceId,
            data
        )
        return result
    
    # 数据更新接口 重写
    def update(self, data):
        # 数据检查
        if not super().exists():
            raise DeviceNotExistException(
                self.userId, 
                self.houseId,
                self.deviceId
            )
        # 执行操作
        result = super().update(data)
        # 发布事件
        publishDeviceUpdateTopic(
            self.userId, 
            self.houseId, 
            self.deviceId,
            parseUpdateData(data)
        )
        return result
    
    # 数据删除接口 重写
    def delete(self):
        # 数据检查
        if not super().exists():
            raise DeviceNotExistException(
                self.userId, 
                self.houseId,
                self.deviceId
            )
        # 执行操作
        result = super().delete()
        # 发布事件
        publishDeviceDeleteTopic(
            self.userId, 
            self.houseId, 
            self.deviceId,
            None
        )
        return result

# 设备位置信息表，存储设备当前在哪个用户的哪个house下面
class DeviceInfoDocument(Document):
    # 重写集合名称
    NAME = COLLECTIONS.deviceInfo

# 设备历史告警 集合类
class DeviceHistoryAlarmsCollection(UserHouseCollection):
    # 重写 name 字段
    NAME = COLLECTIONS.deviceHistoryAlarms

# 设备历史状态数据 集合类
class DeviceHistoryDatasCollection(UserHouseCollection):
    # 重写 name 字段
    NAME = COLLECTIONS.deviceHistoryDatas

# 设备操作日志数据 集合类
class DeviceOperationsCollection(UserHouseCollection):
    # 重写 name 字段
    NAME = COLLECTIONS.deviceOperations

# 设备状态订阅 集合表
class DeviceStateEventSubcriberCollection(Collection):
    # 集合名称
    NAME = COLLECTIONS.deviceStateEventSubcriber


# 即将废弃
class Device:
    # init firestore object
    DB = firestore.Client()

    def __init__(self, userId, houseId, deviceId, 
        deviceVendorPrefix):
        self.userId = userId
        self.houseId = houseId
        self.deviceId = deviceId
        self.deviceVendorPrefix = deviceVendorPrefix
        self.deviceRef = self.getDeviceRef()
        self.collectionRef = self.getCollectionRef()

    # 获取设备数据库引用
    def getDeviceRef(self):
        # # 检查用户
        # userRef = DB.collection(COLLECTIONS.users
        #     ).document(self.userId).get()
        # if not userRef.exists:
        #     raise UserNotExistException(self.userId)
        # # 检查房子
        # houseRef = userRef.collection(COLLECTIONS.houses
        #     ).document(self.houseId).get()
        # if not houseRef.exists:
        #     raise HouseNotExistException(self.userId, self.houseId)
        # 检查设备
        deviceRef = self.DB.collection(COLLECTIONS.users
            ).document(self.userId
            ).collection(COLLECTIONS.houses
            ).document(self.houseId
            ).collection(COLLECTIONS.devices
            ).document(self.deviceId)

        return deviceRef
    
    def getCollectionRef(self):
        colRef = self.DB.collection(COLLECTIONS.users
            ).document(self.userId
            ).collection(COLLECTIONS.houses
            ).document(self.houseId
            ).collection(COLLECTIONS.devices
            )
        return colRef

    # 检查设备引用是否存在
    def isDeviceExist(self):
        return self.deviceRef.get().exists

    # 数据创建接口 封装
    def create(self, data):
        # 数据检查
        # 执行操作
        result = self.deviceRef.create(data)
        # 发布事件
        publishDeviceCreateTopic(
            self.userId, 
            self.houseId, 
            self.deviceId,
            data
        )
        return result
    
    # 数据更新接口 封装
    def update(self, data):
        # 数据检查
        if not self.isDeviceExist():
            raise DeviceNotExistException(
                self.userId, 
                self.houseId,
                self.deviceId
            )
        # 执行操作
        result = self.deviceRef.update(data)
        # 发布事件
        publishDeviceUpdateTopic(
            self.userId, 
            self.houseId, 
            self.deviceId,
            parseUpdateData(data)
        )
        return result
    
    # 数据删除接口 封装
    def delete(self):
        # 数据检查
        if not self.isDeviceExist():
            raise DeviceNotExistException(
                self.userId, 
                self.houseId,
                self.deviceId
            )
        # 执行操作
        result = self.deviceRef.delete()
        # 发布事件
        publishDeviceDeleteTopic(
            self.userId, 
            self.houseId, 
            self.deviceId,
            None
        )
        return result

    def get(self, documentId):
        docRef = self.collectionRef.document(
            documentId)
        if not docRef.get().exists:
            return None
        return docRef.get().to_dict()

    # 数据获取
    # condition = {"fieldName": {"operation": "fieldValue"}}
    def list(self, condition = None):
        fieldName, op, fieldValue = parseCondition(condition)

        if fieldName is not None:
            return map(
                lambda item:item.to_dict(), 
                self.collectionRef.where(
                    fieldName, op, fieldValue).stream()
            )
        
        return map(
            lambda item:item.to_dict(), 
            self.collectionRef.stream()
        )
    
    # 查找并更新
    def findAndUpdate(self, updateData, condition = None):
        fieldName, op, fieldValue = parseCondition(condition)

        stream = None
        if fieldName is not None:
            stream = self.collectionRef.where(
                    fieldName, op, fieldValue).stream()
        else:
            stream = self.collectionRef.stream()
        
        for perDoc in stream:
            perDoc.reference.update(updateData)
# 即将废弃
class DeviceHistoryAlarms:
    # init firestore object
    DB = firestore.Client()

    def __init__(self, userId, houseId):
        self.userId = userId
        self.houseId = houseId
        self.collectionRef = self.getCollectionRef()

    # 获取数据表集合引用
    def getCollectionRef(self):
        colRef = self.DB.collection(COLLECTIONS.users
            ).document(self.userId
            ).collection(COLLECTIONS.houses
            ).document(self.houseId
            ).collection(COLLECTIONS.deviceHistoryAlarms
            )
        return colRef

    # 数据创建接口 封装
    def add(self, data):
        result = self.collectionRef.add(data)
        return result
# 即将废弃
class DeviceHistoryDatas:
    # init firestore object
    DB = firestore.Client()

    def __init__(self, userId, houseId):
        self.userId = userId
        self.houseId = houseId
        self.collectionRef = self.getCollectionRef()

    # 获取数据表集合引用
    def getCollectionRef(self):
        colRef = self.DB.collection(COLLECTIONS.users
            ).document(self.userId
            ).collection(COLLECTIONS.houses
            ).document(self.houseId
            ).collection(COLLECTIONS.deviceHistoryDatas
            )
        return colRef

    # 数据创建接口 封装
    def add(self, data):
        result = self.collectionRef.add(data)
        return result
# 即将废弃
# 设备位置信息表，存储设备当前在哪个用户的哪个house下面
class DeviceInfo:
    # init firestore object
    DB = firestore.Client()

    def __init__(self, deviceId):
        self.deviceId    = deviceId
        self.documentRef = self.getDocumentRef()

    # 获取数据表文档引用
    def getDocumentRef(self):
        docRef = self.DB.collection(COLLECTIONS.deviceInfo
            ).document(self.deviceId)
        return docRef

    # 数据创建接口 封装
    def create(self, data):
        # 使用set，覆盖现有
        result = self.documentRef.set(data)
        return result
    
    # 数据删除接口
    def delete(self):
        result = self.documentRef.delete()
    
    # 获取数据
    def get(self):
        if not self.documentRef.get().exists:
            return None
        return self.documentRef.get().to_dict()
# 即将废弃
# 设备状态订阅 集合表
class DeviceStateEventSubcriber(Collection):
    # 集合名称
    NAME = COLLECTIONS.deviceStateEventSubcriber

    # 重写实现，获取数据表集合引用
    def getCollectionRef(self):
        colRef = self.DB.collection(self.NAME)
        return colRef
