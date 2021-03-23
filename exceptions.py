class UserNotExistException(Exception):
    def __init__(self, userId):
        self.userId = userId
    def __str__(self):
        print("userId:" + self.userId  + " not exist")

class HouseNotExistException(Exception):
    def __init__(self, userId, houseId):
        self.userId = userId
        self.houseId = houseId
    def __str__(self):
        print("userId:" + self.userId  
        + ", houseId:" + self.houseId
        + " not exist")

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

class EnvironmentValueNotFoundException(Exception):
    def __init__(self, envField):
        self.envField = envField
    def __str__(self):
        print("environment value:" + self.envField  + " not found")