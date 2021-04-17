class BaseException(Exception):
    # 异常id
    ID = None

# 用户不存在
class UserNotExistException(BaseException):
    ID = 40001
    def __init__(self, userId):
        self.userId = userId
    def __str__(self):
        return ("userId=" + self.userId)

# 用户房子不存在
class HouseNotExistException(BaseException):
    ID = 40002
    def __init__(self, userId, houseId):
        self.userId = userId
        self.houseId = houseId
    def __str__(self):
        return ("userId=" + self.userId + 
            ", houseId=" + self.houseId)

# 用户房子设备不存在
class DeviceNotExistException(BaseException):
    ID = 40003
    def __init__(self, userId, houseId, deviceId):
        self.userId = userId
        self.houseId = houseId
        self.deviceId = deviceId
    def __str__(self):
        return ("userId=" + self.userId  
        + ", houseId=" + self.houseId
        + ", deviceId=" + self.deviceId)

# 参数未提供
class ParametersNotProvideException(BaseException):
    ID = 40004
    def __init__(self, fieldName):
        self.fieldName = fieldName
    def __str__(self):
        return ("parameterName=" + self.fieldName)

# 环境变量未提供
class EnvironmentValueNotFoundException(BaseException):
    ID = 40005
    def __init__(self, envField):
        self.envField = envField
    def __str__(self):
        print("environmentName=" + self.envField)

# 物联消息参数缺失
class WulianMessageParameterMissingException(BaseException):
    ID = 40006
    def __init__(self, messageField):
        self.messageField = messageField
    def __str__(self):
        print("parameterName=" + self.messageField)

# token未提供
class UserTokenNotProvideException(BaseException):
    ID = 40007
    pass

# token失效
class UserTokenExpireException(BaseException):
    ID = 40008
    pass

# 用户没有萤石子账号
class EzvizAccountNotFoundException(BaseException):
    ID = 40009
    pass
# 用户没有物联子账号
class WulianAccountNotFoundException(BaseException):
    ID = 40010
    pass
# 用户没有涂鸦子账号
class TuyaAccountNotFoundException(BaseException):
    ID = 40011
    pass

# 设备数据模版未注册
class DeviceTypeDataTemplateNotFoundException(BaseException):
    ID = 40012
    pass

# 设备已经存在
class DeviceAlreadyExistException(BaseException):
    ID = 40013
    def __init__(self, userId, houseId, deviceId):
        self.userId   = userId
        self.houseId  = houseId
        self.deviceId = deviceId
    def __str__(self):
        return ("userId=" + self.userId  
        + ", houseId=" + self.houseId
        + ", deviceId=" + self.deviceId)

# 设备厂商不支持
class DeviceVendorNotSupportException(BaseException):
    ID = 40014
    def __init__(self, deviceVendor):
        self.deviceVendor = deviceVendor
    def __str__(self):
        return ("deviceVendor=" + self.deviceVendor)

# 设备已经归属其他人
class DeviceBelongToOthersException(BaseException):
    ID = 40015
    def __init__(self, userId, houseId, deviceId):
        self.userId   = userId
        self.houseId  = houseId
        self.deviceId = deviceId
    def __str__(self):
        return ("userId=" + self.userId  
        + ", houseId=" + self.houseId
        + ", deviceId=" + self.deviceId)

# 设备添加异常
class DeviceAddFailedException(BaseException):
    ID = 40016
    pass

# 设备验证码错误异常
class DeviceVerifyCodeIncorrectException(BaseException):
    ID = 40017
    pass

# 物联接口调用异常
class WulianAPICallException(BaseException):
    ID = 40018
    def __init__(self, errorMessage=None):
        self.errorMessage = errorMessage

# 涂鸦接口调用异常
class TuyaAPICallException(BaseException):
    ID = 40019
    def __init__(self, errorMessage=None):
        self.errorMessage = errorMessage

# 萤石接口调用异常
class EzvizAPICallException(BaseException):
    ID = 40020
    def __init__(self, errorMessage=None):
        self.errorMessage = errorMessage