# 所有设备类别
class DEVICE_CATEGORY:
    # 环境检测器
    environment_sensor = "devices.category.ENVIRONMENT_SENSOR"
    # 安放探测器
    security_detector  = "devices.category.SECURITY_DETECTOR"
    # 智能网关
    smart_gateway      = "devices.category.SMART_GATEWAY"
    # 智能开关
    smart_switch       = "devices.category.SMART_SWITCH"
    # 智能摄像头
    smart_camera       = "devices.category.SMART_CAMERA"

# 所有设备类型
class DEVICE_TYPE:
	# 红外探测器
	pir_detector        = "devices.types.PIR_DETECTOR"
	# 烟雾探测器
	smoke_detector      = "devices.types.SMOKE_DETECTOR"
	# 门窗磁感应器
	contact_detector    = "devices.types.CONTACT_DETECTOR"
	# 水浸探测器
	water_leak_detector = "devices.types.WATER_LEAK_DETECTOR"
	# 天然气探测器
	gas_detector        = "devices.types.GAS_DETECTOR"
	# 光强检测器
	light_sensor        = "devices.types.LIGHT_SENSOR"
	# 温湿度检测器
	temp_humi_sensor    = "devices.types.TEMP_HUMI_SENSOR"
	# 一路墙壁开关
	wall_switch_1       = "devices.types.WALL_SWITCH_1"
	# 两路墙壁开关
	wall_switch_2       = "devices.types.WALL_SWITCH_2"
	# 三路墙壁开关
	wall_switch_3       = "devices.types.WALL_SWITCH_3"
	# 一路零火开关
	embedded_switch_1   = "devices.types.EMBEDDED_SWITCH_1"
	# 两路零火开关
	embedded_switch_2   = "devices.types.EMBEDDED_SWITCH_2"
	# 六路场景开关
	scene_switch_6      = "devices.types.SCENE_SWITCH_6"
	# 车库门控制器
	garage_door_opener  = "devices.types.GARAGE_DOOR_OPENER"
	# 报警器
	sound_warner = "devices.types.SOUND_WARNER"
	# 摄像头，对应萤石
	camera_c3w = "devices.types.CAMERA_C3W"
	camera_c3a = "devices.types.CAMERA_C3A"
	camera_lc1c = "devices.types.CAMERA_LC1C"
	camera_bc1 = "devices.types.CAMERA_BC1"
	camera_w2h = "devices.types.CAMERA_W2H"
	camera_c3x = "devices.types.CAMERA_C3X"
	# 网关，对应物联
	gateway_01 = "devices.types.GATEWAY_01"
	gateway_02 = "devices.types.GATEWAY_02"
	# 窗帘控制器
	curtain_opener = "devices.types.CURTAIN_OPENER"

	# mapping to iconTypeId
	toTypeId = {
		gateway_01: "01",
		gateway_02: "02",
		pir_detector: "03",
		smoke_detector: "04",
		contact_detector: "05",
		water_leak_detector: "06",
		gas_detector: "07",
		wall_switch_1: "08",
		wall_switch_2: "08",
		wall_switch_3: "08",
		scene_switch_6: "09",
		embedded_switch_1: "10",
		embedded_switch_2: "10",
		garage_door_opener: "11",
		camera_c3w: "12",
		camera_c3a: "13",
		camera_lc1c: "12",
		camera_bc1: "12",
		camera_c3x: "12",
		camera_w2h: "01",
		temp_humi_sensor: "14",
		light_sensor: "15",
		sound_warner: "16",
		curtain_opener: "17"
	}

# 设备厂商 代码
class DEVICE_VENDOR:
	# 物联
	WULIAN = "devices.vendor.WULIAN"
	# 萤石
	EZVIZ  = "devices.vendor.EZVIZ"
	# 涂鸦
	TUYA   = "devices.vendor.TUYA"

# 设备厂商 代码前缀
# 该前缀将追加到厂商的设备id，形成sps的设备id
class DEVICE_VENDOR_PREFIX:
	# 物联
	WULIAN = "0001"
	# 萤石
	EZVIZ  = "0002"
	# 涂鸦
	TUYA   = "0003"

# 设备厂商 用户id前缀，用于根据sps user id生成对应厂商的userId
class DEVICE_VENDOR_USERID_PREFIX:
	# 物联
	WULIAN = "wl"
	# 萤石
	EZVIZ  = "ez"
	# 涂鸦
	TUYA   = "ty"

# 传感器类设备的状态常量
class SENSOR_STATE:
	# PIR 红外入侵检测
	HUMAN_PASS_DETECTED = "human_pass_detected"
	NO_HUMAN_PASS_DETECTED = "no_human_pass_detected"
	# CONTACTOR 门窗磁检测器
	CONTACTOR_OPEN_DETECTED = "contactor_open_detected"
	CONTACTOR_CLOSE_DETECTED = "contactor_close_detected"
	# SMOKE 烟雾检测器
	SMOKE_DETECTED = "smoke_detected"
	NO_SMOKE_DETECTED = "no_smoke_detected"
	# WATER LEAK 水浸检测器
	WATER_LEAK_DETECTED = "water_leak_detected"
	NO_WATER_LEAK_DETECTED = "no_water_leak_detected"
	# GAS 天然气检测器
	GAS_DETECTED = "gas_detected"
	NO_GAS_DETECTED = "no_gas_detected"
	# 零火开关 恢复状态设置
	# 即 断电恢复之后，是否恢复断电前的状态
	DO_NOT_RECOVER = "do_not_recover_previous_state"
	RECOVER = "recover_previous_state"

# 所有设备告警
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
	detect_scene_switch_click = "detect_scene_switch_click"
    # 物联消息代码 转换成告警消息
	# message_code_to_alarm = {
	# 	WULIAN_DEVICE_MESSAGE_CODE.device_online     : device_online,
	# 	WULIAN_DEVICE_MESSAGE_CODE.device_offline    : device_offline,
	# 	WULIAN_DEVICE_MESSAGE_CODE.device_set_arm    : device_set_arm,
	# 	WULIAN_DEVICE_MESSAGE_CODE.device_set_disarm : device_set_disarm,
	# 	WULIAN_DEVICE_MESSAGE_CODE.device_is_delete  : device_is_delete,
	# 	WULIAN_DEVICE_MESSAGE_CODE.device_low_power  : device_low_power,
	# 	WULIAN_DEVICE_MESSAGE_CODE.device_is_broken  : device_is_broken,
	# 	WULIAN_DEVICE_MESSAGE_CODE.detect_contact_open  : detect_contact_open,
	# 	WULIAN_DEVICE_MESSAGE_CODE.detect_contact_close : detect_contact_close,
	# 	WULIAN_DEVICE_MESSAGE_CODE.detect_pass : detect_pass,
	# 	WULIAN_DEVICE_MESSAGE_CODE.detect_start_normal_warning : detect_start_normal_warning,
	# 	WULIAN_DEVICE_MESSAGE_CODE.detect_start_fire_warning   : detect_start_fire_warning,
	# 	WULIAN_DEVICE_MESSAGE_CODE.detect_stop_warning : detect_stop_warning,
	# 	WULIAN_DEVICE_MESSAGE_CODE.detect_smoke : detect_smoke,
	# 	WULIAN_DEVICE_MESSAGE_CODE.detect_gas : detect_gas,
	# 	WULIAN_DEVICE_MESSAGE_CODE.detect_water_leak : detect_water_leak,
	# 	WULIAN_DEVICE_MESSAGE_CODE.detect_switch_open : detect_switch_open,
	# 	WULIAN_DEVICE_MESSAGE_CODE.detect_switch_close : detect_switch_close,
	# }

# 所有支持的设备指令类型
class DEVICE_COMMAND:
	# command for traits=action.devices.traits.ArmDisarm
	ARM_DISARM = "action.devices.commands.ArmDisarm" # 设防或者撤防操作
	# command for traits=action.devices.traits.Toggles
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
	CONFIG_MOTION_SOUND     = "action.devices.commands.ConfigMotionSound"
	# 窗帘控制器
	OPEN_CLOSE          = "action.devices.commands.OpenClose"
	OPEN_CLOSE_PERCENT          = "action.devices.commands.OpenClosePercent"
	OPEN_CLOSE_RELATIVE = "action.devices.commands.OpenCloseRelative"

# 执行设备指令的触发源
class EXECUTE_DEVICE_TRIGGER:
    # 由手动执行触发
	MANUAL = "device.trigger.MANUAL"
    # 由自动场景触发
	SCENE = "device.trigger.SCENE"

# 物联设备支持的指令类型
class WULIAN_DEVICE_CMD:
	SYNC = "SYNC"
	GET = "GET"
	DELETE_DEVICE = "DELETE_DEVICE"
	ARM_DISARM = DEVICE_COMMAND.ARM_DISARM
	SET_TOGGLES = DEVICE_COMMAND.SET_TOGGLES
	SWITCH_TOGGLES = DEVICE_COMMAND.SWITCH_TOGGLES
	TOGGLES_STATUS = DEVICE_COMMAND.TOGGLES_STATUS
	ENABLE_RECOVER_MODE = DEVICE_COMMAND.ENABLE_RECOVER_MODE
	DISABLE_RECOVER_MODE = DEVICE_COMMAND.DISABLE_RECOVER_MODE
	RESET_POWER_CONSUMPTION = DEVICE_COMMAND.RESET_POWER_CONSUMPTION
	ELECTRIC_STATUS = DEVICE_COMMAND.ELECTRIC_STATUS

# 萤石设备支持的指令类型
class EZVIZ_DEVICE_CMD:
	SYNC = "SYNC"
	GET = "GET"
	ARM_DISARM = DEVICE_COMMAND.ARM_DISARM
	CONFIG_MOTION_SENTIVITY = DEVICE_COMMAND.CONFIG_MOTION_SENTIVITY
	CONFIG_MOTION_AREA      = DEVICE_COMMAND.CONFIG_MOTION_AREA
	CONFIG_MOTION_SOUND     = DEVICE_COMMAND.CONFIG_MOTION_SOUND

# 涂鸦设备支持的指令类型
class TUYA_DEVICE_CMD:
	SYNC = "SYNC"
	GET  = "GET"
	DELETE = DEVICE_COMMAND.DELETE
	SET_TOGGLES = DEVICE_COMMAND.SET_TOGGLES
	SWITCH_TOGGLES = DEVICE_COMMAND.SWITCH_TOGGLES
	TOGGLES_STATUS = DEVICE_COMMAND.TOGGLES_STATUS
	OPEN_CLOSE          = DEVICE_COMMAND.OPEN_CLOSE
	OPEN_CLOSE_PERCENT  = DEVICE_COMMAND.OPEN_CLOSE_PERCENT
	OPEN_CLOSE_RELATIVE = DEVICE_COMMAND.OPEN_CLOSE_RELATIVE

