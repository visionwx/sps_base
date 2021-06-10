class SupportDevice:
    def __init__(self,
        id,
        groupName,
        rankId,
        enable = True,
        deviceCategorys = [],
    ):
        self.id        = id
        self.groupName = groupName
        self.rankId    = rankId
        self.enable    = enable
        self.deviceCategorys = deviceCategorys
    
    def toDict(self):
        return {
            "groupName": self.groupName,
            "rankId": self.rankId,
            "enable": self.enable,
            "deviceCategorys": list(map(
                lambda dc:dc.toDict(),
                self.deviceCategorys
            )),  
        }
    
    def addDeviceCategory(self, deviceCategory):
        if self.deviceCategorys is None:
            self.deviceCategorys = []
        self.deviceCategorys.append(deviceCategory)

class DeviceCategory:
    def __init__(self,
        id,
        name,
        description = "",
        icon = "",
        enable = True,
        deviceTypes = [],
    ):
        self.id = id
        self.name = name
        self.description = description
        self.icon = icon
        self.enable = enable
        self.deviceTypes = deviceTypes

    def toDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "icon": self.icon,
            "enable": self.enable,
            "deviceTypes": list(map(
                lambda dc:dc.toDict(),
                self.deviceTypes
            )),
        }

    def addDeviceType(self, deviceType):
        if self.deviceTypes is None:
            self.deviceTypes = []
        self.deviceTypes.append(deviceType)

class DeviceType:
    def __init__(self,
        id,
        name,
        icon,
        deviceInfo,
        description = "",
        enable = True,
        pictures = [],
        
    ):
        self.id = id
        self.name = name
        self.description = description
        self.icon = icon
        self.enable = enable
        self.pictures = pictures
        self.deviceInfo = deviceInfo
    
    def toDict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "icon": self.icon,
            "enable": self.enable,
            "pictures": self.pictures,
            "deviceInfo": self.deviceInfo.toDict()
        }

class DeviceInfo:
    def __init__(self,
        manufacturer,
        model,
        hwVersion = None,
        swVersion = None,
    ):
        self.manufacturer = manufacturer
        self.model = model
        self.hwVersion = hwVersion
        self.swVersion = swVersion
    
    def toDict(self):
        return {
            "manufacturer": self.manufacturer,
            "model": self.model,
            "hwVersion": self.hwVersion,
            "swVersion": self.swVersion
        }

from sps_base.utils.parameters import getParaFromEnvironment
from sps_base.devices import DEVICE_TYPE,DEVICE_CATEGORY

# 获取谷歌项目id
projectId = getParaFromEnvironment("GCP_PROJECT")

ICON_URL = "https://storage.googleapis.com/{projectId}.appspot.com/devices/96x96/{deviceTypeId}.png"
ICON_URL = ICON_URL.replace("{projectId}", projectId)
def getIconUrlByDeviceType(deviceType):
    return ICON_URL.replace(
        "{deviceTypeId}", 
        DEVICE_TYPE.toTypeId.get(deviceType, "01")
    )


# 定义所有分类
# 1. 智能网关 大类
deviceCategory_Gateway = DeviceCategory(
    id = DEVICE_CATEGORY.smart_gateway,
    name = "Smart Gateway",
)
# 2. 环境检测器 大类
deviceCategory_Sensor = DeviceCategory(
    id = DEVICE_CATEGORY.environment_sensor,
    name = "Environment Sensor",
)
# 3. 安防检测器 大类
deviceCategory_Detector = DeviceCategory(
    id = DEVICE_CATEGORY.security_detector,
    name = "Security Detector",
)
# 4. 智能开关 大类
deviceCategory_Switch = DeviceCategory(
    id = DEVICE_CATEGORY.smart_switch,
    name = "Smart Switch",
)
# 5. 摄像头 大类
deviceCategory_Camera = DeviceCategory(
    id = DEVICE_CATEGORY.smart_camera,
    name = "Smart Camera",
)
# 6. 门锁 大类
deviceCategory_Locker = DeviceCategory(
    id = DEVICE_CATEGORY.smart_locker,
    name = "Smart Locker",
)



# 定义所有分组： 分组 可以包含多个大类
# 第一个设备组别 定义：
# Smart Gateway
supportDevice_Gateway = SupportDevice(
    id = "0001",
    rankId=1,
    groupName="Smart Gateway",
)
# 第二个设备组别 定义：
# Sensor and detector
supportDevice_SensorAndDetector = SupportDevice(
    id = "0002",
    rankId=2,
    groupName="Sensor and Detector",
)
# 第三个设备组别 定义：
# Smart Switch
supportDevice_Switch = SupportDevice(
    id = "0003",
    rankId=3,
    groupName="Smart Switch",
)
# 第四个设备组别 定义：
# Smart Camera
supportDevice_Camera = SupportDevice(
    id = "0004",
    rankId=4,
    groupName="Smart Camera",
)
# 第五个设备组别 定义：
# Smart Locker
supportDevice_Locker = SupportDevice(
    id = "0005",
    rankId=5,
    groupName="Smart Locker",
)

supportDevices = [
    supportDevice_Gateway,
    supportDevice_SensorAndDetector,
    supportDevice_Switch,
    supportDevice_Camera,
    supportDevice_Locker
]


# 将 category 绑定 到对应的 分组下
supportDevice_Gateway.addDeviceCategory(deviceCategory_Gateway)

supportDevice_SensorAndDetector.addDeviceCategory(deviceCategory_Sensor)
supportDevice_SensorAndDetector.addDeviceCategory(deviceCategory_Detector)

supportDevice_Switch.addDeviceCategory(deviceCategory_Switch)

supportDevice_Camera.addDeviceCategory(deviceCategory_Camera)

supportDevice_Locker.addDeviceCategory(deviceCategory_Locker)



# 添加不同的 deviceType 到 大类下
from . import wulian_gateway
from . import wulian_environment_sensor
from . import wulian_security_detector
from . import wulian_scene_switch
from . import wulian_embedded_switch
from . import wulian_wall_switch
from . import tuya_garage_door_opener
from . import tuya_curtain_opener
from . import tuya_door_locker
from . import ezviz_camera

import pprint
pprint.pprint(supportDevices)