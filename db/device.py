from collections import COLLECTIONS
from sps_base.exceptions import UserNotExistException, HouseNotExistException, DeviceNotExistException
from google.cloud import firestore
from sps_base.pubsub.publisher import publishDeviceCreateTopic, publishDeviceUpdateTopic, publishDeviceDeleteTopic

class DEVICE:
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
        # 检查用户
        userRef = DB.collection(COLLECTIONS.users
            ).document(self.userId).get()
        if not userRef.exists:
            raise UserNotExistException(self.userId)
        # 检查房子
        houseRef = userRef.collection(COLLECTIONS.houses
            ).document(self.houseId).get()
        if not houseRef.exists:
            raise HouseNotExistException(self.userId, self.houseId)
        # 检查设备
        deviceRef = houseRef.collection(COLLECTIONS.devices
            ).document(self.deviceId)
        return deviceRef
    
    # 检查设备引用是否存在
    def isDeviceExist(self):
        if not self.deviceRef.get().exists:
            raise DeviceNotExistException(
                self.userId, 
                self.houseId,
                self.deviceId
            )

    # 数据创建接口 封装
    def create(self, data):
        # 数据检查
        # 执行操作
        result = self.deviceRef.create(data)
        publishDeviceCreateTopic(
            self.userId, self.houseId, self.deviceId,
            data)
        return result
    
    # 数据更新接口 封装
    def update(self, data):
        # 数据检查
        self.isDeviceExist()
        # 执行操作
        result = self.deviceRef.update(data)
        publishDeviceUpdateTopic(
            self.userId, self.houseId, self.deviceId,
            data)
        return result
    
    # 数据删除接口 封装
    def delete(self):
        self.isDeviceExist()
        result = self.deviceRef.delete()
        publishDeviceDeleteTopic(
            self.userId, self.houseId, self.deviceId,
            None)
        return result