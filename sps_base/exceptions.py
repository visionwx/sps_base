# 用户不存在
class UserNotExistException(Exception):
    def __init__(self, userId):
        self.userId = userId
    def __str__(self):
        print("userId:" + self.userId  + " not exist")

# 用户房子不存在
class HouseNotExistException(Exception):
    def __init__(self, userId, houseId):
        self.userId = userId
        self.houseId = houseId
    def __str__(self):
        print("userId:" + self.userId  
        + ", houseId:" + self.houseId
        + " not exist")

# 用户房子设备不存在
class DeviceNotExistException(Exception):
    def __init__(self, userId, houseId, deviceId):
        self.userId = userId
        self.houseId = houseId
        self.deviceId = deviceId
    def __str__(self):
        print("userId:" + self.userId  
        + ", houseId:" + self.houseId
        + ", deviceId:" + self.deviceId  
        + " not exist")

# 参数未提供
class ParametersNotProvideException(Exception):
    def __init__(self, fieldName):
        self.fieldName = fieldName
    def __str__(self):
        print("parameter:" + self.fieldName  + " not found")

# 环境变量未提供
class EnvironmentValueNotFoundException(Exception):
    def __init__(self, envField):
        self.envField = envField
    def __str__(self):
        print("environment value:" + self.envField  + " not found")

# 物联消息参数缺失
class WulianMessageParameterMissingException(Exception):
    def __init__(self, messageField):
        self.messageField = messageField
    def __str__(self):
        print("Wulian message parameter:" + self.messageField  + " missing")