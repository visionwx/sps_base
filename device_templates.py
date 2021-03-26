import copy
from sps_base.utils.parameters import getParaFromEnvironment
from sps_base.devices import DEVICE_CATEGORY, DEVICE_TYPE, DEVICE_VENDOR
from sps_base.wulian import WULIAN_DEVICE_TYPE
from sps_base.device_states import HUMAN_PASS_STATE,SMOKE_STATE,WATER_LEAK_STATE,CONTACT_STATE,GAS_STATE

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

# PIR
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
    devData["attributes"] = {
        "sensorStatesSupported": [{
            "name": "humanPassDetectState",
            "descriptiveCapabilities": {
                "availableStates": [ 
                    HUMAN_PASS_STATE.HUMAN_PASS_DETECTED, 
                    HUMAN_PASS_STATE.NO_HUMAN_PASS_DETECTED
                ]
            },
            "updateTime": None, #<timestamp_when_this_state_is_update>
        }]
    }
    return devData

# Contactor
def generateContactorTemplate_WULIAN():
    devData = copy.deepcopy(BASE_TEMPLATE)
    devData["category"] = DEVICE_CATEGORY.security_detector
    devData["type"]  = DEVICE_TYPE.contact_detector
    devData["icons"] = generateIconsUrlConfig(DEVICE_TYPE.contact_detector)
    devData["googleType"] = "action.devices.types.SENSOR"
    devData["name"] = {
        "defaultName": ["Smart Contact Detector"],
        "name": "Smart Contact Detector",
        "nicknames": ["Smart Contact Detector"]
    }
    devData["deviceInfo"] = {
        "manufacturer": DEVICE_VENDOR.WULIAN,
        "productPicture": None,
        "model": "WL-ZSPDBPW-MT-02",
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
            "contactDetectState": CONTACT_STATE.CONTACTOR_CLOSE_DETECTED
        }
    }
    devData["attributes"] = {
        "sensorStatesSupported": [{
            "name": "contactDetectState",
            "descriptiveCapabilities": {
                "availableStates": [ 
                    CONTACT_STATE.CONTACTOR_OPEN_DETECTED, 
                    CONTACT_STATE.CONTACTOR_CLOSE_DETECTED
                ]
            },
            "updateTime": None, #<timestamp_when_this_state_is_update>
        }]
    }
    return devData

# Smoker
def generateSmokerTemplate_WULIAN():
    devData = copy.deepcopy(BASE_TEMPLATE)
    devData["category"] = DEVICE_CATEGORY.security_detector
    devData["type"]  = DEVICE_TYPE.smoke_detector
    devData["icons"] = generateIconsUrlConfig(DEVICE_TYPE.smoke_detector)
    devData["googleType"] = "action.devices.types.SENSOR"
    devData["name"] = {
        "defaultName": ["Honeywell Smoke Detector"],
        "name": "Honeywell Smoke Detector",
        "nicknames": ["Honeywell Smoke Detector"]
    }
    devData["deviceInfo"] = {
        "manufacturer": DEVICE_VENDOR.WULIAN,
        "productPicture": None,
        "model": "JTYJ-GD-2690/W",
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
            "contactDetectState": SMOKE_STATE.NO_SMOKE_DETECTED
        }
    }
    devData["attributes"] = {
        "sensorStatesSupported": [{
            "name": "contactDetectState",
            "descriptiveCapabilities": {
                "availableStates": [ 
                    SMOKE_STATE.SMOKE_DETECTED, 
                    SMOKE_STATE.NO_SMOKE_DETECTED
                ]
            },
            "updateTime": None, #<timestamp_when_this_state_is_update>
        }]
    }
    return devData

# WaterLeaker
def generateWaterLeakerTemplate_WULIAN():
    devData = copy.deepcopy(BASE_TEMPLATE)
    devData["category"] = DEVICE_CATEGORY.security_detector
    devData["type"]  = DEVICE_TYPE.water_leak_detector
    devData["icons"] = generateIconsUrlConfig(DEVICE_TYPE.water_leak_detector)
    devData["googleType"] = "action.devices.types.SENSOR"
    devData["name"] = {
        "defaultName": ["Water Leakage Detector"],
        "name": "Water Leakage Detector",
        "nicknames": ["Water Leakage Detector"]
    }
    devData["deviceInfo"] = {
        "manufacturer": DEVICE_VENDOR.WULIAN,
        "productPicture": None,
        "model": "WL-ZSSMBPW-FD-01",
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
            "contactDetectState": WATER_LEAK_STATE.NO_WATER_LEAK_DETECTED
        }
    }
    devData["attributes"] = {
        "sensorStatesSupported": [{
            "name": "contactDetectState",
            "descriptiveCapabilities": {
                "availableStates": [ 
                    WATER_LEAK_STATE.WATER_LEAK_DETECTED, 
                    WATER_LEAK_STATE.NO_WATER_LEAK_DETECTED
                ]
            },
            "updateTime": None, #<timestamp_when_this_state_is_update>
        }]
    }
    return devData

# GAS Detector
def generateGASTemplate_WULIAN():
    devData = copy.deepcopy(BASE_TEMPLATE)
    devData["category"] = DEVICE_CATEGORY.security_detector
    devData["type"]  = DEVICE_TYPE.gas_detector
    devData["icons"] = generateIconsUrlConfig(DEVICE_TYPE.gas_detector)
    devData["googleType"] = "action.devices.types.SENSOR"
    devData["name"] = {
        "defaultName": ["Gas Leakage Detector"],
        "name": "Gas Leakage Detector",
        "nicknames": ["Gas Leakage Detector"]
    }
    devData["deviceInfo"] = {
        "manufacturer": DEVICE_VENDOR.WULIAN,
        "productPicture": None,
        "model": "WL-ZSSMBPW-FD-01",
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
            "contactDetectState": GAS_STATE.NO_GAS_DETECTED
        }
    }
    devData["attributes"] = {
        "sensorStatesSupported": [{
            "name": "contactDetectState",
            "descriptiveCapabilities": {
                "availableStates": [ 
                    GAS_STATE.GAS_DETECTED, 
                    GAS_STATE.NO_GAS_DETECTED
                ]
            },
            "updateTime": None, #<timestamp_when_this_state_is_update>
        }]
    }
    return devData

# TEMP HUMI 
# Light

# WALL_SW_1,2,3

# EMBEDED_SW_1,2

# SCENE_SW_6

# GARAGE_DOOR

# 

class DeviceTemplates:
    PIR_WULIAN           = generatePIRTemplate_WULIAN()
    CONTACTOR_WULIAN     = generateContactorTemplate_WULIAN()
    SMOKER_WULIAN        = generateSmokerTemplate_WULIAN()
    WATER_LEAKER_WULIAN  = generateWaterLeakerTemplate_WULIAN()
    GAS_WULIAN           = generateGASTemplate_WULIAN()
    TEMP_HUMI_WULIAN     = None
    LIGHT_WULIAN         = None
    WALL_SWITCH_1_WULIAN = None
    WALL_SWITCH_2_WULIAN = None
    WALL_SWITCH_3_WULIAN = None
    EMBEDDED_SWITCH_1_WULIAN = None
    EMBEDDED_SWITCH_2_WULIAN = None
    SCENE_SWITCH_6_WULIAN    = None
    GARAGE_DOOR_OPENER_TUYA  = None
    CAMERA_C3W_EZVIZ = None
    CAMERA_C3A_EZVIZ = None