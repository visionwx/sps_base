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

# token未提供
class UserTokenNotProvideException(Exception):
    pass

# token失效
class UserTokenExpireException(Exception):
    pass

# 用户没有萤石子账号
class EzvizAccountNotFoundException(Exception):
    pass
# 用户没有物联子账号
class WulianAccountNotFoundException(Exception):
    pass
# 用户没有涂鸦子账号
class TuyaAccountNotFoundException(Exception):
    pass

# 设备数据模版未注册
class DeviceTypeDataTemplateNotFoundException(Exception):
    pass

# 设备已经存在
class DeviceAlreadyExistException(Exception):
    def __init__(self, userId, houseId, deviceId):
        self.userId   = userId
        self.houseId  = houseId
        self.deviceId = deviceId

# 设备厂商不支持
class DeviceVendorNotSupportException(Exception):
    def __init__(self, deviceVendor):
        self.deviceVendor = deviceVendor

# 设备已经归属其他人
class DeviceBelongToOthersException(Exception):
    def __init__(self, userId, houseId, deviceId):
        self.userId   = userId
        self.houseId  = houseId
        self.deviceId = deviceId

# 设备添加异常
class DeviceAddFailedException(Exception):
    pass