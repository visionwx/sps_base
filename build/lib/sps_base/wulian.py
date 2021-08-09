from sps_base.devices import DEVICE_ALARM,DEVICE_TYPE

# 物联mqtt订阅消息主题类型
class WULIAN_MQTT_SUBSCRIBE_TOPIC:
    DATA  = "DATA"
    STATE = "STATE"
    ALARM = "ALARM"

    @staticmethod
    def generateWulianTopicId(wulianPartnerId, wulianTopicType):
        return "wl/partner/" + wulianPartnerId +  "/" + wulianTopicType.lower()

# 物联设备 消息代码
class WULIAN_DEVICE_MESSAGE_CODE:
	device_online  = "0101012"
	device_offline = "0101022"
	device_set_arm = "0102012"
	device_set_disarm = "0102022"
	device_is_delete  = "0101021"
	device_low_power  = "0101031"
	device_is_broken  = "0101041"
	detect_contact_open  = "0102051"
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

# 物联设备 消息代码 到 SPS告警类型的 mapping
WULIAN_DEVICE_ALARMS = {
    WULIAN_DEVICE_MESSAGE_CODE.device_online     : DEVICE_ALARM.device_online,
    WULIAN_DEVICE_MESSAGE_CODE.device_offline    : DEVICE_ALARM.device_offline,
    WULIAN_DEVICE_MESSAGE_CODE.device_set_arm    : DEVICE_ALARM.device_set_arm,
    WULIAN_DEVICE_MESSAGE_CODE.device_set_disarm : DEVICE_ALARM.device_set_disarm,
    WULIAN_DEVICE_MESSAGE_CODE.device_is_delete  : DEVICE_ALARM.device_is_delete,
    WULIAN_DEVICE_MESSAGE_CODE.device_low_power  : DEVICE_ALARM.device_low_power,
    WULIAN_DEVICE_MESSAGE_CODE.device_is_broken  : DEVICE_ALARM.device_is_broken,
    WULIAN_DEVICE_MESSAGE_CODE.detect_contact_open  : DEVICE_ALARM.detect_contact_open,
    WULIAN_DEVICE_MESSAGE_CODE.detect_contact_close : DEVICE_ALARM.detect_contact_close,
    WULIAN_DEVICE_MESSAGE_CODE.detect_pass : DEVICE_ALARM.detect_pass,
    WULIAN_DEVICE_MESSAGE_CODE.detect_start_normal_warning : DEVICE_ALARM.detect_start_normal_warning,
    WULIAN_DEVICE_MESSAGE_CODE.detect_start_fire_warning   : DEVICE_ALARM.detect_start_fire_warning,
    WULIAN_DEVICE_MESSAGE_CODE.detect_stop_warning : DEVICE_ALARM.detect_stop_warning,
    WULIAN_DEVICE_MESSAGE_CODE.detect_smoke : DEVICE_ALARM.detect_smoke,
    WULIAN_DEVICE_MESSAGE_CODE.detect_gas : DEVICE_ALARM.detect_gas,
    WULIAN_DEVICE_MESSAGE_CODE.detect_water_leak : DEVICE_ALARM.detect_water_leak,
    WULIAN_DEVICE_MESSAGE_CODE.detect_switch_open : DEVICE_ALARM.detect_switch_open,
    WULIAN_DEVICE_MESSAGE_CODE.detect_switch_close : DEVICE_ALARM.detect_switch_close,
}

# 物联开关设备类型代码 到 sps设备类型代码的 mapping
WULIAN_SWITCH_TYPE = {
	"61": "devices.types.WALL_SWITCH_1",
	"62": "devices.types.WALL_SWITCH_2",
	"63": "devices.types.WALL_SWITCH_3",
}

# 物联网关设备类型代码 到 sps设备类型代码的 mapping
WULIAN_GW_TYPE = {
	"GW01" : "devices.types.GATEWAY_01",
	"GW06" : "devices.types.GATEWAY_02"
}

# SPS设备类型 到 物联设备类型代码的 mapping
WULIAN_DEVICE_TYPE = {
	DEVICE_TYPE.gas_detector: "09",
	DEVICE_TYPE.pir_detector: "02",
	DEVICE_TYPE.contact_detector: "03",
	DEVICE_TYPE.water_leak_detector: "06",
	DEVICE_TYPE.smoke_detector: "43",
	DEVICE_TYPE.sound_warner: "01",
	DEVICE_TYPE.temp_humi_sensor: "17",
	DEVICE_TYPE.light_sensor: "19",
	DEVICE_TYPE.scene_switch_6: "37",
	DEVICE_TYPE.embedded_switch_1: "Aj",
	DEVICE_TYPE.embedded_switch_2: "At",
	DEVICE_TYPE.wall_switch_1: "61",
	DEVICE_TYPE.wall_switch_2: "62",
	DEVICE_TYPE.wall_switch_3: "63",
	DEVICE_TYPE.wall_outlet_1: "Dy",
	DEVICE_TYPE.wall_outlet_2: "Dy",
	DEVICE_TYPE.wall_outlet_3: "Dy",
}

class WULIAN_RECOVER_STATE:
	DO_NOT_RECOVER = "do_not_recover_previous_state"
	RECOVER = "recover_previous_state"

class WULIAN_HUMAN_PASS_STATE:
	HUMAN_PASS_DETECTED = "human_pass_detected"
	NO_HUMAN_PASS_DETECTED = "no_human_pass_detected"