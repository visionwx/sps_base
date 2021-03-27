import copy
from sps_base.utils.parameters import getParaFromEnvironment
from sps_base.devices import DEVICE_CATEGORY, DEVICE_TYPE, DEVICE_VENDOR
from sps_base.wulian import WULIAN_DEVICE_TYPE
from sps_base.device_states import HUMAN_PASS_STATE,SMOKE_STATE,WATER_LEAK_STATE,CONTACT_STATE,GAS_STATE,RECOVER_STATE

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
            "smokeDetectState": SMOKE_STATE.NO_SMOKE_DETECTED
        }
    }
    devData["attributes"] = {
        "sensorStatesSupported": [{
            "name": "smokeDetectState",
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
            "waterLeakDetectState": WATER_LEAK_STATE.NO_WATER_LEAK_DETECTED
        }
    }
    devData["attributes"] = {
        "sensorStatesSupported": [{
            "name": "waterLeakDetectState",
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
            "gasDetectState": GAS_STATE.NO_GAS_DETECTED
        }
    }
    devData["attributes"] = {
        "sensorStatesSupported": [{
            "name": "gasDetectState",
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
def generateTempHumiTemplate_WULIAN():
    devData = copy.deepcopy(BASE_TEMPLATE)
    devData["category"] = DEVICE_CATEGORY.environment_sensor
    devData["type"]  = DEVICE_TYPE.temp_humi_sensor
    devData["icons"] = generateIconsUrlConfig(DEVICE_TYPE.temp_humi_sensor)
    devData["googleType"] = "action.devices.types.SENSOR"
    devData["name"] = {
        "defaultName": ["Temperature Humidity Sensor"],
        "name": "Temperature Humidity Sensor",
        "nicknames": ["Temperature Humidity Sensor"]
    }
    devData["deviceInfo"] = {
        "manufacturer": DEVICE_VENDOR.WULIAN,
        "productPicture": None,
        "model": "WL-ZSSMBPW-FD-01",
        "hwVersion": None,
        "swVersion": None
    }
    devData["traits"] = [
        "action.devices.traits.SensorState"
    ]
    devData["states"] = {
        "online": False,
        "currentSensorStateData": {
            "humidityAmbientPercent": None,
            "temperatureAmbientCelsius": None
        }
    }
    devData["attributes"] = {
        "sensorStatesSupported": [
            {
                "name": "humidityAmbientPercent",
                "numericCapabilities": {
                    "rawValueUnit": "%",
                    "rawValueRange": {
                        "min": 0,
                        "max": 100
                    }
                },
                "updateTime": None, #<timestamp_when_this_state_is_update>
            },
            {
                "name": "temperatureAmbientCelsius",
                "numericCapabilities": {
                    "rawValueUnit": "C",
                    "rawValueRange": {
                        "min": -100,
                        "max": 100
                    }
                },
                "updateTime": None, #<timestamp_when_this_state_is_update>
            }
        ]
    }
    return devData

# Light
def generateLightTemplate_WULIAN():
    devData = copy.deepcopy(BASE_TEMPLATE)
    devData["category"] = DEVICE_CATEGORY.environment_sensor
    devData["type"]  = DEVICE_TYPE.light_sensor
    devData["icons"] = generateIconsUrlConfig(DEVICE_TYPE.light_sensor)
    devData["googleType"] = "action.devices.types.SENSOR"
    devData["name"] = {
        "defaultName": ["Light Sensor"],
        "name": "Light Sensor",
        "nicknames": ["Light Sensor"]
    }
    devData["deviceInfo"] = {
        "manufacturer": DEVICE_VENDOR.WULIAN,
        "productPicture": None,
        "model": "WL-ZSSMBPW-FD-01",
        "hwVersion": None,
        "swVersion": None
    }
    devData["traits"] = [
        "action.devices.traits.SensorState"
    ]
    devData["states"] = {
        "online": False,
        "currentSensorStateData": {
            "humidityAmbientPercent": None,
            "temperatureAmbientCelsius": None
        }
    }
    devData["attributes"] = {
        "sensorStatesSupported": [
            {
                "name": "brightness",
                "numericCapabilities": {
                    "rawValueUnit": "Lx",
                    "rawValueRange": {
                        "min": 0,
                        "max": 1000
                    }
                },
                "updateTime": None, #<timestamp_when_this_state_is_update>
            }
        ]
    }
    return devData

# WALL_SW_1,2,3
def generateToggleConfig(numOfToggles):
    currentToggleSettings = {}
    availableToggles = []
    for i in range(numOfToggles):
        i += 1
        data = {
            "name": "switch" + str(i),
            "name_values": [ 
                {
                    "name_synonym": ["switch" + str(i)],
                    "lang": "en"
                }
            ]
        }
        availableToggles.append(data)
        currentToggleSettings["switch" + str(i)] = False
    return currentToggleSettings,availableToggles

def generateWallSwitchTemplate_WULIAN(numOfToggles):
    if numOfToggles > 3:
        raise Exception("numOfTogglesExceed")
    _name = ["One", "Two", "Three"]
    _type = [DEVICE_TYPE.wall_switch_1, DEVICE_TYPE.wall_switch_2, DEVICE_TYPE.wall_switch_3]
    currentToggleSettings,availableToggles = generateToggleConfig(numOfToggles)

    devData = copy.deepcopy(BASE_TEMPLATE)
    devData["category"] = DEVICE_CATEGORY.smart_switch
    devData["type"]  = _type[numOfToggles]
    devData["icons"] = generateIconsUrlConfig(_type[numOfToggles])
    devData["googleType"] = "action.devices.types.SENSOR"
    devData["name"] = {
        "defaultName": [_name[numOfToggles - 1] + "-Gang Wall Switch"],
        "name": _name[numOfToggles - 1] + "-Gang Wall Switch",
        "nicknames": [_name[numOfToggles - 1] + "-Gang Wall Switch"]
    }
    devData["deviceInfo"] = {
        "manufacturer": DEVICE_VENDOR.WULIAN,
        "productPicture": None,
        "model": "WL-ZCSWNPW-S1322-01",
        "hwVersion": None,
        "swVersion": None
    }
    devData["traits"] = [
        "action.devices.traits.Toggles"
    ]
    devData["states"] = {
        "online": False,
        "currentToggleSettings": currentToggleSettings
    }
    devData["attributes"] = {
        "availableToggles": availableToggles,
    }
    return devData

# EMBEDED_SW_1,2
eletricalStatesSupported = [
	{
		"name": "current",
		"numericCapabilities": {
			"rawValueUnit": "A",
			"rawValueRange": {
				"min": 0,
				"max": 1000
			}
		},
	},
	{
		"name": "voltage",
		"numericCapabilities": {
			"rawValueUnit": "V",
			"rawValueRange": {
				"min": 0,
				"max": 10000
			}
		},
	},
	{
		"name": "realTimePower",
		"numericCapabilities": {
			"rawValueUnit": "W",
			"rawValueRange": {
				"min": 0,
				"max": 10000
			}
		},
	},
	{
		"name": "powerConsumption",
		"numericCapabilities": {
			"rawValueUnit": "kW/h",
			"rawValueRange": {
				"min": 0,
				"max": 10000
			}
		},
	},
	{
		"name": "recoverMode",
		"descriptiveCapabilities": {
			"availableStates": [ RECOVER_STATE.DO_NOT_RECOVER, RECOVER_STATE.RECOVER ]
		},
	},
]
def generateEmbeddedSwitchTemplate_WULIAN(numOfToggles):
    if numOfToggles > 2:
        raise Exception("numOfTogglesExceed")
    _name = ["One", "Two"]
    _type = [DEVICE_TYPE.embedded_switch_1, DEVICE_TYPE.embedded_switch_2]
    currentToggleSettings,availableToggles = generateToggleConfig(numOfToggles)

    devData = copy.deepcopy(BASE_TEMPLATE)
    devData["category"] = DEVICE_CATEGORY.smart_switch
    devData["type"]  = _type(numOfToggles)
    devData["icons"] = generateIconsUrlConfig(_type(numOfToggles))
    devData["googleType"] = "action.devices.types.SENSOR"
    devData["name"] = {
        "defaultName": [_name[numOfToggles - 1] + "-Gang Embedded Switch"],
        "name": _name[numOfToggles - 1] + "-Gang Embedded Switch",
        "nicknames": [_name[numOfToggles - 1] + "-Gang Embedded Switch"]
    }
    devData["deviceInfo"] = {
        "manufacturer": DEVICE_VENDOR.WULIAN,
        "productPicture": None,
        "model": "WL-ZCSENPB-S0410-02",
        "hwVersion": None,
        "swVersion": None
    }
    devData["traits"] = [
        "action.devices.traits.Toggles",
        "action.devices.traits.Electric"
    ]
    devData["states"] = {
        "online": False,
        "currentToggleSettings": currentToggleSettings,
        "currentElectricalData": {
            "voltage": None,
            "current": None,
            "realTimePower": None,
            "powerConsumption": None,
            "recoverMode": RECOVER_STATE.RECOVER
        }
    }
    devData["attributes"] = {
        "availableToggles": availableToggles,
    }
    return devData

# SCENE_SW_6
def generateSceneSwitchTemplate_WULIAN():
    devData = copy.deepcopy(BASE_TEMPLATE)
    devData["category"] = DEVICE_CATEGORY.smart_switch
    devData["type"]  = DEVICE_TYPE.scene_switch_6
    devData["icons"] = generateIconsUrlConfig(DEVICE_TYPE.scene_switch_6)
    devData["googleType"] = "action.devices.types.SENSOR"
    devData["name"] = {
        "defaultName": ["Scene Switch"],
        "name": "Scene Switch",
        "nicknames": ["Scene Switch"]
    }
    devData["deviceInfo"] = {
        "manufacturer": DEVICE_VENDOR.WULIAN,
        "productPicture": None,
        "model": "WL-ZGCRNPW-S3011-02",
        "hwVersion": None,
        "swVersion": None
    }
    devData["traits"] = [
        "action.devices.traits.SceneTrigger",
    ]
    devData["states"] = {
        "online": False,
        "currentSceneSwitchStates": {
            "switch1": None,
            "switch2": None,
            "switch3": None,
            "switch4": None,
            "switch5": None,
            "switch6": None
        }
    }
    devData["attributes"] = {
        "availableSceneSwitches": [
            {
                "name": "switch1",
                "binding_scene": None  # {"scene_id": <scene_id>, "scene_name": <scene_name>, "scene_icon": <scene_icon>}
            },
            {
                "name": "switch2",
                "binding_scene": None
            },
            {
                "name": "switch3",
                "binding_scene": None
            },
            {
                "name": "switch4",
                "binding_scene": None
            },
            {
                "name": "switch5",
                "binding_scene": None
            },
            {
                "name": "switch6",
                "binding_scene": None
            }
        ],
    }
    return devData

# GARAGE_DOOR

# 

class DeviceTemplates:
    PIR_WULIAN           = generatePIRTemplate_WULIAN()
    CONTACTOR_WULIAN     = generateContactorTemplate_WULIAN()
    SMOKER_WULIAN        = generateSmokerTemplate_WULIAN()
    WATER_LEAKER_WULIAN  = generateWaterLeakerTemplate_WULIAN()
    GAS_WULIAN           = generateGASTemplate_WULIAN()
    TEMP_HUMI_WULIAN     = generateTempHumiTemplate_WULIAN()
    LIGHT_WULIAN         = generateLightTemplate_WULIAN()
    WALL_SWITCH_1_WULIAN = generateWallSwitchTemplate_WULIAN(1)
    WALL_SWITCH_2_WULIAN = generateWallSwitchTemplate_WULIAN(2)
    WALL_SWITCH_3_WULIAN = generateWallSwitchTemplate_WULIAN(3)
    EMBEDDED_SWITCH_1_WULIAN = generateEmbeddedSwitchTemplate_WULIAN(1)
    EMBEDDED_SWITCH_2_WULIAN = generateEmbeddedSwitchTemplate_WULIAN(2)
    SCENE_SWITCH_6_WULIAN    = generateSceneSwitchTemplate_WULIAN()
    GARAGE_DOOR_OPENER_TUYA  = None
    CURTAIN_TUYA = None
    CAMERA_C3W_EZVIZ = None
    CAMERA_C3A_EZVIZ = None

    # @classmethod
    # def fromType(cls, deviceType):
    #     if deviceType == DEVICE_TYPE.pir_detector:
    #         return cls.PIR_WULIAN
    #     elif deviceType == DEVICE_TYPE.contact_detector:
    #         return cls.CONTACTOR_WULIAN
    #     elif deviceType == DEVICE_TYPE.smoke_detector:
    #         return cls.SMOKER_WULIAN
    #     elif deviceType == DEVICE_TYPE.water_leak_detector:
    #         return cls.WATER_LEAKER_WULIAN
    #     elif deviceType == DEVICE_TYPE.contact_detector:
    #         return cls.GAS_WULIAN
    #     elif deviceType == DEVICE_TYPE.contact_detector:
    #         return cls.TEMP_HUMI_WULIAN
    #     elif deviceType == DEVICE_TYPE.contact_detector:
    #         return cls.LIGHT_WULIAN
    #     elif deviceType == DEVICE_TYPE.contact_detector:
    #         return cls.WALL_SWITCH_1_WULIAN
    #     elif deviceType == DEVICE_TYPE.contact_detector:
    #         return cls.WALL_SWITCH_2_WULIAN
    #     elif deviceType == DEVICE_TYPE.contact_detector:
    #         return cls.WALL_SWITCH_3_WULIAN
    #     elif deviceType == DEVICE_TYPE.contact_detector:
    #         return cls.EMBEDDED_SWITCH_1_WULIAN
    #     elif deviceType == DEVICE_TYPE.contact_detector:
    #         return cls.EMBEDDED_SWITCH_2_WULIAN
    #     elif deviceType == DEVICE_TYPE.contact_detector:
    #         return cls.SCENE_SWITCH_6_WULIAN
    #     elif deviceType == DEVICE_TYPE.contact_detector:
    #         return cls.GARAGE_DOOR_OPENER_TUYA
    #     elif deviceType == DEVICE_TYPE.contact_detector:
    #         return cls.CAMERA_C3W_EZVIZ
    #     elif deviceType == DEVICE_TYPE.contact_detector:
    #         return cls.CAMERA_C3A_EZVIZ
    #     return None