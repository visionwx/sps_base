class COLLECTIONS:
	users = "users"
	vendor = "vendor"
	user_tokens = "user_tokens"
	deviceInfo = "deviceInfo"
	emailCodes = "emailCodes"
	supportDevices = "supportDevices"
	deviceDataModel = "deviceDataModel"
	supportDeviceStateEvents = "supportDeviceStateEvents"
	supportDeviceStateCommands = "supportDeviceStateCommands"
	supportSceneConditionTypes = "supportSceneConditionTypes"
	houses = "houses"
	devices = "devices"                         #  users->houses->
	scenes = "scenes"                           #  users->houses->
	rooms = "rooms"                             #  users->houses->
	messages = "messages"                       #  users->houses->
	deviceHistoryAlarms = "deviceHistoryAlarms" #  users->houses->
	deviceHistoryDatas = "deviceHistoryDatas"   #  users->houses->
	deviceOperations = "deviceOperations"       #  users->houses->

class DEVICE_CATEGORY:
	environment_sensor = "devices.category.ENVIRONMENT_SENSOR"
	security_detector = "devices.category.SECURITY_DETECTOR"
	smart_gateway = "devices.category.SMART_GATEWAY"
	smart_switch = "devices.category.SMART_SWITCH"
	smart_camera = "devices.category.SMART_CAMERA"

class DEVICE_TYPE:
	pir_detector = "devices.types.PIR_DETECTOR"
	smoke_detector = "devices.types.SMOKE_DETECTOR"
	contact_detector = "devices.types.CONTACT_DETECTOR"
	water_leak_detector = "devices.types.WATER_LEAK_DETECTOR"
	gas_detector = "devices.types.GAS_DETECTOR"
	light_sensor = "devices.types.LIGHT_SENSOR"
	temp_humi_sensor = "devices.types.TEMP_HUMI_SENSOR"
	wall_switch_1 = "devices.types.WALL_SWITCH_1"
	wall_switch_2 = "devices.types.WALL_SWITCH_2"
	wall_switch_3 = "devices.types.WALL_SWITCH_3"
	embedded_switch_1 = "devices.types.EMBEDDED_SWITCH_1"
	embedded_switch_2 = "devices.types.EMBEDDED_SWITCH_2"
	scene_switch_6 = "devices.types.SCENE_SWITCH_6"

class SENSOR_STATE:
	# PIR
	HUMAN_PASS_DETECTED = "human_pass_detected"
	NO_HUMAN_PASS_DETECTED = "no_human_pass_detected"
	# CONTACTOR
	CONTACTOR_OPEN_DETECTED = "contactor_open_detected"
	CONTACTOR_CLOSE_DETECTED = "contactor_close_detected"
	# SMOKE
	SMOKE_DETECTED = "smoke_detected"
	NO_SMOKE_DETECTED = "no_smoke_detected"
	# WATER LEAK
	WATER_LEAK_DETECTED = "water_leak_detected"
	NO_WATER_LEAK_DETECTED = "no_water_leak_detected"
	# GAS
	GAS_DETECTED = "gas_detected"
	NO_GAS_DETECTED = "no_gas_detected"

# wulian device message code
class DEVICE_MESSAGE_CODE:
	device_online = "0101012"
	device_offline = "0101022"
	device_set_arm = "0102012"
	device_set_disarm = "0102022"
	device_is_delete = "0101021"
	device_low_power = "0101031"
	device_is_broken = "0101041"
	detect_contact_open = "0102051"
	detect_contact_close = "0102111"
	detect_pass = "0102011"
	detect_start_normal_warning = "0102032"
	detect_start_fire_warning = "0102042"
	detect_stop_warning = "0102052"
	detect_smoke = "0102041"
	detect_gas = "0102031"
	detect_water_leak = "0102021"
	detect_switch_open = "0106012"
	detect_switch_close = "0106022"

class DEVICE_ALARM:
	device_online     = "device_online"
	device_offline    = "device_offline"
	device_set_arm    = "device_set_arm"
	device_set_disarm = "device_set_disarm"
	device_is_delete  = "device_is_delete"
	device_low_power  = "device_low_power"
	device_is_broken  = "device_is_broken"
	detect_contact_open  = "detect_contact_open"
	detect_contact_close = "detect_contact_close"
	detect_pass = "detect_pass"
	detect_pass_cancel = "detect_pass_cancel"
	detect_start_normal_warning = "detect_start_normal_warning"
	detect_start_fire_warning   = "detect_start_fire_warning"
	detect_stop_warning = "detect_stop_warning"
	detect_smoke = "detect_smoke"
	detect_gas = "detect_gas"
	detect_water_leak = "detect_water_leak"
	detect_switch_open = "detect_switch_open"
	detect_switch_close = "detect_switch_close"
	message_code_to_alarm = {
		DEVICE_MESSAGE_CODE.device_online     : device_online,
		DEVICE_MESSAGE_CODE.device_offline    : device_offline,
		DEVICE_MESSAGE_CODE.device_set_arm    : device_set_arm,
		DEVICE_MESSAGE_CODE.device_set_disarm : device_set_disarm,
		DEVICE_MESSAGE_CODE.device_is_delete  : device_is_delete,
		DEVICE_MESSAGE_CODE.device_low_power  : device_low_power,
		DEVICE_MESSAGE_CODE.device_is_broken  : device_is_broken,
		DEVICE_MESSAGE_CODE.detect_contact_open  : detect_contact_open,
		DEVICE_MESSAGE_CODE.detect_contact_close : detect_contact_close,
		DEVICE_MESSAGE_CODE.detect_pass : detect_pass,
		DEVICE_MESSAGE_CODE.detect_start_normal_warning : detect_start_normal_warning,
		DEVICE_MESSAGE_CODE.detect_start_fire_warning   : detect_start_fire_warning,
		DEVICE_MESSAGE_CODE.detect_stop_warning : detect_stop_warning,
		DEVICE_MESSAGE_CODE.detect_smoke : detect_smoke,
		DEVICE_MESSAGE_CODE.detect_gas : detect_gas,
		DEVICE_MESSAGE_CODE.detect_water_leak : detect_water_leak,
		DEVICE_MESSAGE_CODE.detect_switch_open : detect_switch_open,
		DEVICE_MESSAGE_CODE.detect_switch_close : detect_switch_close,
	}

class DEVICE_VENDOR:
	WULIAN = "devices.vendor.WULIAN"
	EZVIZ = "devices.vendor.EZVIZ"
	TUYA = "devices.vendor.TUYA"

class DEVICE_VENDOR_PREFIX:
	WULIAN = "0001"
	EZVIZ  = "0002"
	TUYA   = "0003"
	
class DEVICE_COMMAND:
	# command for traits=action.devices.traits.ArmDisarm
	ARM_DISARM = "action.devices.commands.ArmDisarm" # 设防或者撤防操作
	# command for traits=action.devices.traints.Toggles
	SET_TOGGLES = "action.devices.commands.SetToggles" # 开光打开，或者关闭
	SWITCH_TOGGLES = "action.devices.commands.SwitchToggles" # 开关切换
	TOGGLES_STATUS = "action.devices.commands.TogglesStatus" # 开关状态更新
	# command for traits=action.devices.traits.Electric
	ENABLE_RECOVER_MODE = "action.devices.commands.EnableRecoverMode" # 启用断电恢复后，恢复到断电前的开关状态
	DISABLE_RECOVER_MODE = "action.devices.commands.DisableRecoverMode" # 禁用断电恢复后，恢复到断电前的开关状态，保持关闭状态
	RESET_POWER_CONSUMPTION = "action.devices.commands.ResetPowerConsumption" # 清楚当前累计用电量
	ELECTRIC_STATUS = "action.devices.commands.ElectricStatus" # 当前电气状态更新
	# command for device mgmt
	DELETE = "DELETE_DEVICE"
	SYNC   = "SYNC"
	GET    = "GET"
	# EZVIZ 动作检测配置
	CONFIG_MOTION_SENTIVITY = "action.devices.commands.ConfigMotionSentivity"
	CONFIG_MOTION_AREA      = "action.devices.commands.ConfigMotionArea"
	CONFIG_MOTION_SOUND      = "action.devices.commands.ConfigMotionSound"

class EXECUTE_DEVICE_TRIGGER:
	MANUAL = "device.trigger.MANUAL"
	SCENE = "device.trigger.SCENE"

class WULIAN_DEVICE_TOPIC:
	DATA = "DATA"
	STATE = "STATE"
	ALARM = "ALARM"
	WULIAN_EXECUTE_DEVICE_TOPIC = "wulian-execute-device"

class EZVIZ_DEVICE_TOPIC:
	EZVIZ_EXECUTE_DEVICE_TOPIC = "ezviz-execute-device"

class WULIAN_DEVICE_CMD:
	SYNC = "SYNC"
	DELETE_DEVICE = "DELETE_DEVICE"
	ARM_DISARM = DEVICE_COMMAND.ARM_DISARM
	SET_TOGGLES = DEVICE_COMMAND.SET_TOGGLES
	SWITCH_TOGGLES = DEVICE_COMMAND.SWITCH_TOGGLES
	TOGGLES_STATUS = DEVICE_COMMAND.TOGGLES_STATUS
	ENABLE_RECOVER_MODE = DEVICE_COMMAND.ENABLE_RECOVER_MODE
	DISABLE_RECOVER_MODE = DEVICE_COMMAND.DISABLE_RECOVER_MODE
	RESET_POWER_CONSUMPTION = DEVICE_COMMAND.RESET_POWER_CONSUMPTION
	ELECTRIC_STATUS = DEVICE_COMMAND.ELECTRIC_STATUS

class EZVIZ_DEVICE_CMD:
	SYNC = "SYNC"
	GET = "GET"
	ARM_DISARM = DEVICE_COMMAND.ARM_DISARM
	CONFIG_MOTION_SENTIVITY = DEVICE_COMMAND.CONFIG_MOTION_SENTIVITY
	CONFIG_MOTION_AREA      = DEVICE_COMMAND.CONFIG_MOTION_AREA
	CONFIG_MOTION_SOUND     = DEVICE_COMMAND.CONFIG_MOTION_SOUND

class TUYA_DEVICE_CMD:
	SYNC = "SYNC"
	GET  = "GET"
	DELETE = DEVICE_COMMAND.DELETE
	SET_TOGGLES = DEVICE_COMMAND.SET_TOGGLES
	SWITCH_TOGGLES = DEVICE_COMMAND.SWITCH_TOGGLES
	TOGGLES_STATUS = DEVICE_COMMAND.TOGGLES_STATUS


class DEVICE_TOPIC:
	DEVICE_CREATE = "device-create"
	DEVICE_STATE_UPDATE = "device-state-update"
	DEVICE_DELETE = "device-delete"
	WULIAN_EXECUTE_DEVICE = "wulian-execute-device"
	EXECUTE_DEVICE = "execute-device"
	EZVIZ_EXECUTE_DEVICE = "ezviz-execute-device"
	TUYA_EXECUTE_DEVICE  = "tuya-execute-device"

# wulian switch type and sps switch type mapping.
WULIAN_SWITCH_TYPE = {
	"61": "devices.types.WALL_SWITCH_1",
	"62": "devices.types.WALL_SWITCH_2",
	"63": "devices.types.WALL_SWITCH_3",
}

WULIAN_GW_TYPE = {
	"GW01" : "devices.types.GATEWAY_01",
	"GW06" : "devices.types.GATEWAY_02"
}

WULIAN_DEVICE_TYPE = {
	"devices.types.GAS_DETECTOR": "09",
	"devices.types.PIR_DETECTOR": "02",
	"devices.types.CONTACT_DETECTOR": "03",
	"devices.types.WATER_LEAK_DETECTOR": "06",
	"devices.types.SMOKE_DETECTOR": "43",
	"devices.types.SOUND_WARNER": "01",
	"devices.types.TEMP_HUMI_SENSOR": "17",
	"devices.types.LIGHT_SENSOR": "19",
	"devices.types.SCENE_SWITCH_6": "37",
	"devices.types.EMBEDDED_SWITCH_1": "Aj",
	"devices.types.EMBEDDED_SWITCH_2": "At",
	"devices.types.WALL_SWITCH_1": "61",
	"devices.types.WALL_SWITCH_2": "62",
	"devices.types.WALL_SWITCH_3": "63"
}

class RECOVER_STATE:
	DO_NOT_RECOVER = "do_not_recover_previous_state"
	RECOVER = "recover_previous_state"

class HUMAN_PASS_STATE:
	HUMAN_PASS_DETECTED = "human_pass_detected"
	NO_HUMAN_PASS_DETECTED = "no_human_pass_detected"