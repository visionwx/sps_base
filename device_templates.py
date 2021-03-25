import copy
from sps_base.utils.parameters import getParaFromEnvironment
from sps_base.devices import DEVICE_CATEGORY, DEVICE_TYPE, DEVICE_VENDOR
from sps_base.wulian import WULIAN_DEVICE_TYPE
from sps_base.device_states import HUMAN_PASS_STATE

# 获取谷歌项目id
projectId = getParaFromEnvironment("GCP_PROJECT")

ICON_URL = "https://storage.googleapis.com/{projectId}.appspot.com/devices/{size}/{deviceTypeId}.png"
ICON_URL = ICON_URL.replace("{projectId}", projectId)

# 生成设备icon url配置
def generateIconsUrlConfig(deviceType): 
    sizes = {
        "small": "24x24", 
        "median": "32x32", 
        "large": "48x48", 
        "superLarge": "96x96"
    }
    _deviceTypeId = DEVICE_TYPE.toTypeId.get(deviceType, "00")
    iconUrl = ICON_URL.replace(
        "{deviceTypeId}", 
        _deviceTypeId
    )
    return dict([(k, iconUrl.replace("{size}", 
        size)) for k,size in sizes.items()])

# 设备数据模型基础格式
BASE_TEMPLATE = {
    "category": None,
    "type": None,
    "icons": None,
    "googleType": None,
    "enableGoogleSync": True,
    "name": {
        "defaultName": [],
        "name": None,
        "nicknames": []
    },
    "deviceInfo": {
        "manufacturer": None,
        "productPicture": None,
        "model": None,
        "hwVersion": None,
        "swVersion": None
    },
    "willReportState": True,
    "attributes": None,
    "traits": [],
    "otherDeviceIds": None,
    "gatewayDeviceId": None,
    "customData": None,
    "room": None,
    "roomHint": None,
    "error": None,
    "alarm": None,
    "states": None
}

def generatePIRTemplate_WULIAN():
    devData = copy.deepcopy(BASE_TEMPLATE)
    devData["category"] = DEVICE_CATEGORY.security_detector
    devData["type"]  = DEVICE_TYPE.pir_detector
    devData["icons"] = generateIconsUrlConfig(DEVICE_TYPE.pir_detector)
    devData["googleType"] = "action.devices.types.SENSOR"
    devData["name"] = {
        "defaultName": ["Smart PIR Motion Detector"],
        "name": "Smart PIR Motion Detector",
        "nicknames": ["Smart PIR Motion Detector"]
    }
    devData["deviceInfo"] = {
        "manufacturer": DEVICE_VENDOR.WULIAN,
        "productPicture": None,
        "model": "WL-ZSPWBPW-PI11-02",
        "hwVersion": None,
        "swVersion": None
    }
    devData["traits"] = [
        "action.devices.traits.ArmDisarm", 
        "action.devices.traits.SensorState"
    ]
    devData["states"] = {
        "online": False,
        "isArmed": True,
        "currentSensorStateData": {
            "humanPassDetectState": HUMAN_PASS_STATE.NO_HUMAN_PASS_DETECTED
        }
    }
    return devData

class DeviceTemplates:
    PIR_WULIAN = generatePIRTemplate_WULIAN()
    CONTACTOR_WULIAN = None
    SMOKER_WULIAN = None
    WATER_LEAKER_WULIAN = None
    GAS_WULIAN = None
    TEMP_HUMI_WULIAN = None
    LIGHT_WULIAN = None
    WALL_SWITCH_1_WULIAN = None
    WALL_SWITCH_2_WULIAN = None
    WALL_SWITCH_3_WULIAN = None
    EMBEDDED_SWITCH_1_WULIAN = None
    EMBEDDED_SWITCH_2_WULIAN = None
    SCENE_SWITCH_6_WULIAN   = None
    GARAGE_DOOR_OPENER_TUYA = None
    CAMERA_C3W_EZVIZ = None
    CAMERA_C3A_EZVIZ = None