from sps_base.collections import COLLECTIONS
from sps_base.exceptions import UserNotExistException, HouseNotExistException, DeviceNotExistException
from google.cloud import firestore
from sps_base.pubsub.publisher import publishDeviceCreateTopic, publishDeviceUpdateTopic, publishDeviceDeleteTopic

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
        deviceRef = DB.collection(COLLECTIONS.users
            ).document(self.userId
            ).collection(COLLECTIONS.houses
            ).document(self.houseId
            ).collection(COLLECTIONS.devices
            ).document(self.deviceId)

        return deviceRef
    
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

class DeviceHistoryAlarms:
    # init firestore object
    DB = firestore.Client()

    def __init__(self, userId, houseId):
        self.userId = userId
        self.houseId = houseId
        self.collectionRef = self.getCollectionRef()

    # 获取数据表集合引用
    def getCollectionRef(self):
        colRef = DB.collection(COLLECTIONS.users
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

class DeviceHistoryDatas:
    # init firestore object
    DB = firestore.Client()

    def __init__(self, userId, houseId):
        self.userId = userId
        self.houseId = houseId
        self.collectionRef = self.getCollectionRef()

    # 获取数据表集合引用
    def getCollectionRef(self):
        colRef = DB.collection(COLLECTIONS.users
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

class DeviceInfo:
    # init firestore object
    DB = firestore.Client()

    def __init__(self, deviceId):
        self.deviceId    = deviceId
        self.documentRef = self.getDocumentRef()

    # 获取数据表文档引用
    def getDocumentRef(self):
        docRef = DB.collection(COLLECTIONS.deviceInfo
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