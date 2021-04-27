import copy
from functools import wraps
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
    devData["type"]  = _type[numOfToggles-1]
    devData["icons"] = generateIconsUrlConfig(_type[numOfToggles-1])
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
    devData["type"]  = _type[numOfToggles-1]
    devData["icons"] = generateIconsUrlConfig(_type[numOfToggles-1])
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
        "eletricalStatesSupported": eletricalStatesSupported
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

# GARAGE DOOR OPENER
def generateGarageDoorOpenerTemplate_TUYA():
    devData = copy.deepcopy(BASE_TEMPLATE)
    devData["category"] = DEVICE_CATEGORY.smart_switch
    devData["type"]  = DEVICE_TYPE.garage_door_opener
    devData["icons"] = generateIconsUrlConfig(DEVICE_TYPE.garage_door_opener)
    devData["googleType"] = "action.devices.types.SENSOR"
    devData["name"] = {
        "defaultName": ["Tuya Garage Door Opener"],
        "name": "Tuya Garage Door Opener",
        "nicknames": ["Tuya Garage Door Opener"]
    }
    devData["deviceInfo"] = {
        "manufacturer": DEVICE_VENDOR.TUYA,
        "productPicture": None,
        "model": "GD-DC5",
        "hwVersion": None,
        "swVersion": None
    }
    devData["traits"] = [
        "action.devices.traits.Toggles",
    ]
    devData["states"] = {
        "online": False,
        "currentToggleSettings": {"switch1": False},
    }
    devData["attributes"] = {
        "availableToggles": [
            {
                "name": "switch1",
                "name_values": [ 
                    {
                        "name_synonym": ["switch1"],
                        "lang": "en"
                    }
                ]
            }
        ],
    }
    return devData

# CURTAIN OPENER
def generateCurtainOpenerTemplate_TUYA():
    devData = copy.deepcopy(BASE_TEMPLATE)
    devData["category"] = DEVICE_CATEGORY.smart_switch
    devData["type"]  = DEVICE_TYPE.curtain_opener
    devData["icons"] = generateIconsUrlConfig(DEVICE_TYPE.curtain_opener)
    devData["googleType"] = "action.devices.types.SENSOR"
    devData["name"] = {
        "defaultName": ["Blinds Controller"],
        "name": "Blinds Controller",
        "nicknames": ["Blinds Controllerr"]
    }
    devData["deviceInfo"] = {
        "manufacturer": DEVICE_VENDOR.TUYA,
        "productPicture": None,
        "model": "3r8gc33pnqsxfe1g",
        "hwVersion": None,
        "swVersion": None
    }
    devData["traits"] = [
        "action.devices.traits.OpenClose",
    ]
    devData["states"] = {
        "online": False,
        "openState": {
            "openPercent": 30,
            "openStatus": "stop", # open/close/stop/opening/closing
            "openDirection": "DOWN"
        },
    }
    devData["attributes"] = {
        "discreteOnlyOpenClose": False,
        "openDirection": ["UP", "DOWN", "LEFT", "RIGHT", "IN", "OUT"],
        "commandOnlyOpenClose": False,
        "queryOnlyOpenClose": False
    }
    return devData

# 增加 SmartDetect 特性
def addSmartDetectTraits(deviceData, supportHuman=False, supportCar=False):
    # 增加traits
    deviceData["traits"].append("action.devices.traits.SmartDetect")
    # 初始化状态值
    deviceData["states"]["currentSmartDetectStates"] = {
        "enable": True,
        "detectType": 3,
        "motionSentivity": 3,
        "alarmSoundType": 0
    }
    # 初始化属性值
    deviceData["attributes"]["smartDetectSupported"] = {
        "supportTypes": [
            {"name": "only motion", "value":3,},
        ],
        "supportMotionSentivity": [
            {"name": "low", "value": 0,},
            {"name": "medium", "value": 3,},
            {"name": "high", "value": 6,},
        ],
        "supportAlarmSoundTypes": [
            {"name": "short", "value": 0,},
            {"name": "long", "value": 1,},
            {"name": "silent", "value": 2,},
        ],
        "motionAreaConfiguration": None,  # [{"topLeftPoint": [], "botRightPoint": []},],
        "crossBorderConfiguration": None, # [{startPoint: [], endPoint: [], direction: 1},],
    }
    if supportHuman:
        deviceData["attributes"]["smartDetectSupported"]["supportTypes"] = [
            {"name": "only motion", "value":3,},
            {"name": "only human", "value":1,},
        ]
    if supportCar:
        deviceData["attributes"]["smartDetectSupported"]["supportTypes"] = [
            {"name": "only motion", "value":3,},
            {"name": "only human", "value":1,},
            {"name": "only car", "value":2,},
            {"name": "human and car", "value":0,},
        ]
    return deviceData

# 增加 NightVision 特性
def addNightVisionTraits(deviceData, supportSpotLight=False):
    # 增加traits
    deviceData["traits"].append("action.devices.traits.NightVision")
    # 初始化状态
    deviceData["states"]["currentNightVisionStates"] = {
        "spotLightMode": 2,
        "spotLightBrightness": 50,
        "irLightMode": 0,
        "irLightSensitivity": 2,
    }
    # 初始化属性
    deviceData["attributes"]["nightVisionSupported"] = {
        "supportIRLightMode": [
            {"name": "Smart Mode(Recommended)", "value": 0, "description": "Auto-Switch Day/Night Mode."},
            {"name": "Enforcing Day Mode", "value": 1, "description": "IR-Light stays off."},
            {"name": "Enforcing Night Mode", "value": 2, "description": "IR-Light stays on."},
        ],
        "supportIRLightSensitivity": [
            {"name": "Low", "value": 1, "description": "Low Sensitivity"},
            {"name": "Medium", "value": 2, "description": "Medium Sensitivity"},
            {"name": "High", "value": 3, "description": "High Sensitivity"},
        ],
    }
    if supportSpotLight:
        deviceData["attributes"]["nightVisionSupported"]["supportSpotLightMode"] = [
            {"name": "Smart Mode(Recommended)", "value": 2, "description": "Black/White mode by default, Switch to color mode when motion detected."},
            {"name": "Black/White Mode", "value": 0, "description": "IR Light, of high invisibility and the image is black and white."},
            {"name": "Color Mode", "value": 1, "description": "Warm light, can be used as night light and the image is colorful."},
        ]
        deviceData["attributes"]["nightVisionSupported"]["supportSpotLightBrightnessRange"] = [0, 100]
        
    return deviceData

# 增加 LiveVideo 特性
def addLiveVideoTraits(deviceData):
    # 增加traits
    deviceData["traits"].append("action.devices.traits.LiveVideo")
    # 初始化状态
    deviceData["states"]["currentLiveVideoStates"] = {
        "encryptVideo": True, # 是否加密视频
        "flipImage": False,    # 是否翻转画面
        "enableMicro": True, # 是否开启麦克风
    }
    return deviceData

# 增加 Battery 特性
def addBatteryTraits(deviceData):
    # 增加traits
    deviceData["traits"].append("action.devices.traits.Battery")
    # 初始化状态
    deviceData["states"]["currentBatteryStates"] = {
        "avaliablePower": 50, # 剩余用电量
        "workMode": 0,        # 电池工作模式
    }
    # 初始化属性值
    deviceData["attributes"]["batterySupported"] = {
        "supportWorkMode": [
            {"name": "save power", "value": 0,},
            {"name": "performance mode", "value": 1,},
        ],
    }
    return deviceData

# 增加 sd卡存储 特性
def addSDStorageTraits(deviceData):
    # 增加traits
    deviceData["traits"].append("action.devices.traits.SDStorage")
    # 初始化状态
    deviceData["states"]["currentSDStorageStates"] = {
        "status": -1, # sd卡工作状态， -1表示没有插入sd卡
    }
    return deviceData

# 增加 云存储 特性
def addCloudStorageTraits(deviceData):
    # 增加traits
    deviceData["traits"].append("action.devices.traits.CloudStorage")
    # 初始化状态
    deviceData["states"]["currentCloudStorageStates"] = {
        "status": -1, # 云存储工作状态， -1表示没有购买套餐
    }
    # 初始化属性值
    # "name": "套餐名称", "expireDate": "套餐到期日期"
    deviceData["attributes"]["cloudStorageSupported"] = None
    return deviceData

# 增加 FloodLight 特性
def addFloodLightTraits(deviceData):
    # 增加traits
    deviceData["traits"].append("action.devices.traits.FloodLight")
    # 初始化状态
    deviceData["states"]["currentFloodLightStates"] = {
        "brightness": 30, # 当前亮度
    }
    # 初始化属性值
    # "name": "套餐名称", "expireDate": "套餐到期日期"
    deviceData["attributes"]["floodLightSupported"] = {
        # 庭院灯自动开启/关闭设置
        # [
        #     {
        #         "startTime": 19,
        #         "endTime": 7,
        #         "repeat": [1,2,3,4,5,6,7], # 1-7 分别代表周一 到 周日
        #     }
        # ]
        "scheduleConfig": None,
    }
    return deviceData

# 生成萤石摄像头数据模版
def generateCameraTemplate_EZVIZ(deviceType, deviceName):
    devData = copy.deepcopy(BASE_TEMPLATE)
    devData["category"] = DEVICE_CATEGORY.smart_camera
    devData["type"]  = deviceType
    devData["icons"] = generateIconsUrlConfig(deviceType)
    devData["googleType"] = "action.devices.types.CAMERA"
    devData["name"] = {
        "defaultName": [deviceName],
        "name": deviceName,
        "nicknames": [deviceName]
    }
    devData["deviceInfo"] = {
        "manufacturer": DEVICE_VENDOR.EZVIZ,
        "productPicture": None,
        "model": "3r8gc33pnqsxfe1g",
        "hwVersion": None,
        "swVersion": None
    }
    devData["traits"] = []
    devData["states"] = {
        "online": False,
    }
    devData["attributes"] = {}
    return devData

# EZVIZ C3W
def generateC3WTemplate_EZVIZ():
    devData = generateCameraTemplate_EZVIZ(
        DEVICE_TYPE.camera_c3w, "C3W Camera")
    # 增加特性
    devData = addSmartDetectTraits(devData)
    devData = addNightVisionTraits(devData, supportSpotLight=True)
    devData = addLiveVideoTraits(devData)
    devData = addSDStorageTraits(devData)
    devData = addCloudStorageTraits(devData)
    return devData

# EZVIZ C3A
def generateC3ATemplate_EZVIZ():
    devData = generateCameraTemplate_EZVIZ(
        DEVICE_TYPE.camera_c3a, "C3A Camera")
    # 增加特性
    devData = addSmartDetectTraits(devData)
    devData = addNightVisionTraits(devData)
    devData = addLiveVideoTraits(devData)
    devData = addSDStorageTraits(devData)
    devData = addCloudStorageTraits(devData)
    return devData

# EZVIZ C3X
def generateC3XTemplate_EZVIZ():
    devData = generateCameraTemplate_EZVIZ(
        DEVICE_TYPE.camera_c3x, "C3X Camera")
    # 增加特性
    devData = addSmartDetectTraits(devData, supportHuman=True, supportCar=True)
    devData = addNightVisionTraits(devData, supportSpotLight=True)
    devData = addLiveVideoTraits(devData)
    devData = addSDStorageTraits(devData)
    devData = addCloudStorageTraits(devData)
    return devData

# EZVIZ LC1C
def generateLC1CTemplate_EZVIZ():
    devData = generateCameraTemplate_EZVIZ(
        DEVICE_TYPE.camera_lc1c, "LC1C Camera")
    # 增加特性
    devData = addSmartDetectTraits(devData)
    devData = addNightVisionTraits(devData, supportSpotLight=False)
    devData = addLiveVideoTraits(devData)
    devData = addSDStorageTraits(devData)
    devData = addCloudStorageTraits(devData)
    devData = addFloodLightTraits(devData)
    return devData

# EZVIZ BC1
def generateBC1Template_EZVIZ():
    devData = generateCameraTemplate_EZVIZ(
        DEVICE_TYPE.camera_bc1, "BC1 Camera")
    # 增加特性
    devData = addSmartDetectTraits(devData, supportHuman=True)
    devData = addNightVisionTraits(devData, supportSpotLight=True)
    devData = addLiveVideoTraits(devData)
    devData = addSDStorageTraits(devData)
    devData = addCloudStorageTraits(devData)
    return devData

# EZVIZ Camera base station
def generateCameraGatewayW2HTemplate_EZVIZ():
    devData = copy.deepcopy(BASE_TEMPLATE)
    devData["category"] = DEVICE_CATEGORY.smart_gateway
    devData["type"]  = DEVICE_TYPE.camera_w2h
    devData["icons"] = generateIconsUrlConfig(DEVICE_TYPE.camera_w2h)
    devData["googleType"] = None
    devData["name"] = {
        "defaultName": ["Camera Base Station"],
        "name": "Camera Base Station",
        "nicknames": ["Camera Base Station"]
    }
    devData["deviceInfo"] = {
        "manufacturer": DEVICE_VENDOR.EZVIZ,
        "productPicture": None,
        "model": "CS-BC1",
        "hwVersion": None,
        "swVersion": None
    }
    devData["traits"] = []
    devData["states"] = {
        "online": False,
    }
    devData["attributes"] = {}
    return devData

# WULIAN GW01/02
def generateGateway01Template_WULIAN():
    devData = copy.deepcopy(BASE_TEMPLATE)
    devData["category"] = DEVICE_CATEGORY.smart_gateway
    devData["type"]  = DEVICE_TYPE.gateway_01
    devData["icons"] = generateIconsUrlConfig(DEVICE_TYPE.gateway_01)
    devData["googleType"] = None
    devData["name"] = {
        "defaultName": ["Wulian Gateway [LAN,AP]"],
        "name": "Wulian Gateway [LAN,AP]",
        "nicknames": ["Wulian Gateway [LAN,AP]"]
    }
    devData["deviceInfo"] = {
        "manufacturer": DEVICE_VENDOR.WULIAN,
        "productPicture": None,
        "model": "WL-ZGWMDPB-G110-05",
        "hwVersion": None,
        "swVersion": None
    }
    devData["traits"] = []
    devData["states"] = {
        "online": False,
    }
    devData["attributes"] = {}
    return devData

# WULIAN GW01/02
def generateGateway02Template_WULIAN():
    devData = copy.deepcopy(BASE_TEMPLATE)
    devData["category"] = DEVICE_CATEGORY.smart_gateway
    devData["type"]  = DEVICE_TYPE.gateway_02
    devData["icons"] = generateIconsUrlConfig(DEVICE_TYPE.gateway_02)
    devData["googleType"] = None
    devData["name"] = {
        "defaultName": ["Wulian Gateway [LAN]"],
        "name": "Wulian Gateway [LAN]",
        "nicknames": ["Wulian Gateway [LAN]"]
    }
    devData["deviceInfo"] = {
        "manufacturer": DEVICE_VENDOR.WULIAN,
        "productPicture": None,
        "model": "WL-ZGWMDPB-G100-0",
        "hwVersion": None,
        "swVersion": None
    }
    devData["traits"] = []
    devData["states"] = {
        "online": False,
    }
    devData["attributes"] = {}
    return devData

class DeviceTemplates:
    # 设备数据模版生成函数容器，按照设备类型保存
    TYPES = {}

    # 设备数据模版函数 注册器
    @classmethod
    def registerTemplatesFuncsByDeviceType(cls, deviceType):
        def decorator(func):
            cls.TYPES[deviceType] = func
            @wraps(func)
            def wrapper(*args, **kwargs):
                return func(*args, **kwargs)
            return wrapper
        return decorator
    
    # 基于设备类型获取 设备数据模版
    @classmethod
    def fromType(cls, deviceType):
        templateFunc = cls.TYPES.get(deviceType, None)
        if templateFunc is None:
            return None
        return templateFunc()

    # 下面的方法后面即将废弃
    # 物联网关gw01
    GATEWAY01_WULIAN = generateGateway01Template_WULIAN()
    GATEWAY02_WULIAN = generateGateway02Template_WULIAN()
    # 获取红外入侵检测器数据模版
    PIR_WULIAN           = generatePIRTemplate_WULIAN()
    # 获取门窗磁感应器数据模版
    CONTACTOR_WULIAN     = generateContactorTemplate_WULIAN()
    # 获取烟雾检测器数据模版
    SMOKER_WULIAN        = generateSmokerTemplate_WULIAN()
    # 获取水浸检测器数据模版
    WATER_LEAKER_WULIAN  = generateWaterLeakerTemplate_WULIAN()
    # 获取天然气检测器数据模版
    GAS_WULIAN           = generateGASTemplate_WULIAN()
    # 获取温湿度检测器数据模版
    TEMP_HUMI_WULIAN     = generateTempHumiTemplate_WULIAN()
    # 获取光强检测器数据模版
    LIGHT_WULIAN         = generateLightTemplate_WULIAN()
    # 获取墙壁开关数据模版，1，2，3分别代表1联，2联，3联开关
    WALL_SWITCH_1_WULIAN = generateWallSwitchTemplate_WULIAN(1)
    WALL_SWITCH_2_WULIAN = generateWallSwitchTemplate_WULIAN(2)
    WALL_SWITCH_3_WULIAN = generateWallSwitchTemplate_WULIAN(3)
    # 获取零火开关数据模版，1，2分别代表1联，2联开关
    EMBEDDED_SWITCH_1_WULIAN = generateEmbeddedSwitchTemplate_WULIAN(1)
    EMBEDDED_SWITCH_2_WULIAN = generateEmbeddedSwitchTemplate_WULIAN(2)
    # 获取场景开关数据模版
    SCENE_SWITCH_6_WULIAN    = generateSceneSwitchTemplate_WULIAN()
    # 获取车库门控制器数据模版
    GARAGE_DOOR_OPENER_TUYA  = generateGarageDoorOpenerTemplate_TUYA()
    # 获取窗帘控制器数据模版
    CURTAIN_TUYA = generateCurtainOpenerTemplate_TUYA()
    CAMERA_C3W_EZVIZ  = generateC3WTemplate_EZVIZ()
    CAMERA_C3A_EZVIZ  = generateC3ATemplate_EZVIZ()
    CAMERA_C3X_EZVIZ  = generateC3XTemplate_EZVIZ()
    CAMERA_LC1C_EZVIZ = generateLC1CTemplate_EZVIZ()
    CAMERA_BC1_EZVIZ  = generateBC1Template_EZVIZ()
    CAMERA_W2H_EZVIZ  = generateCameraGatewayW2HTemplate_EZVIZ()

# 获取红外入侵检测器数据模版
@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.pir_detector)
def pir():
    return generatePIRTemplate_WULIAN()

# 获取门窗磁感应器数据模版
@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.contact_detector)
def contact():
    return generateContactorTemplate_WULIAN()

# 获取水浸检测器数据模版
@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.water_leak_detector)
def water():
    return generateWaterLeakerTemplate_WULIAN()

# 获取烟雾检测器数据模版
@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.smoke_detector)
def smoke():
    return generateSmokerTemplate_WULIAN()

# 获取天然气检测器数据模版
@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.gas_detector)
def gas():
    return generateGASTemplate_WULIAN()

# 获取温湿度检测器数据模版
@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.temp_humi_sensor)
def temp_humi():
    return generateTempHumiTemplate_WULIAN()

# 获取光强检测器数据模版
@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.light_sensor)
def light():
    return generateLightTemplate_WULIAN()

# 获取墙壁开关数据模版，1，2，3分别代表1联，2联，3联开关
@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.wall_switch_1)
def wall_sw_1():
    return generateWallSwitchTemplate_WULIAN(1)

@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.wall_switch_2)
def wall_sw_2():
    return generateWallSwitchTemplate_WULIAN(2)

@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.wall_switch_3)
def wall_sw_3():
    return generateWallSwitchTemplate_WULIAN(3)

# 获取零火开关数据模版，1，2分别代表1联，2联开关
@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.embedded_switch_1)
def embedded_switch_1():
    return generateEmbeddedSwitchTemplate_WULIAN(1)

@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.embedded_switch_2)
def embedded_switch_2():
    return generateEmbeddedSwitchTemplate_WULIAN(2)


# 获取场景开关数据模版
@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.scene_switch_6)
def scene_switch_6():
    return generateSceneSwitchTemplate_WULIAN()

# 获取车库门控制器数据模版
@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.garage_door_opener)
def garage_door_opener():
    return generateGarageDoorOpenerTemplate_TUYA()

# 获取窗帘控制器数据模版
@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.curtain_opener)
def curtain_opener():
    return generateCurtainOpenerTemplate_TUYA()

# 获取萤石摄像头数据模版
@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.camera_c3w)
def camera_c3w():
    return generateC3WTemplate_EZVIZ()

@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.camera_c3a)
def camera_c3a():
    return generateC3ATemplate_EZVIZ()

@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.camera_c3x)
def camera_c3x():
    return generateC3XTemplate_EZVIZ()

@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.camera_lc1c)
def camera_lc1c():
    return generateLC1CTemplate_EZVIZ()

@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.camera_bc1)
def camera_bc1():
    return generateBC1Template_EZVIZ()

@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.camera_w2h)
def camera_w2h():
    return generateCameraGatewayW2HTemplate_EZVIZ()

@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.gateway_01)
def gateway_01():
    return generateGateway01Template_WULIAN()

@DeviceTemplates.registerTemplatesFuncsByDeviceType(DEVICE_TYPE.gateway_02)
def gateway_02():
    return generateGateway02Template_WULIAN()
