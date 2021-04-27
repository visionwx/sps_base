class WULIAN_DEVICE_TOPIC:
	DATA  = "DATA"
	STATE = "STATE"
	ALARM = "ALARM"
	WULIAN_EXECUTE_DEVICE_TOPIC = "wulian-execute-device"

class EZVIZ_DEVICE_TOPIC:
	EZVIZ_EXECUTE_DEVICE_TOPIC = "ezviz-execute-device"

# 设备相关主题
class DEVICE_TOPIC:
    # 设备新建时 触发
    CREATE = "device-create"
    # 设备状态更新时 触发
    STATE_UPDATE = "device-state-update"
    # 设备删除时 触发
    DELETE = "device-delete"
    # 执行设备指令时 触发
    EXECUTE        = "execute-device"
    WULIAN_EXECUTE = "wulian-execute-device"
    EZVIZ_EXECUTE  = "ezviz-execute-device"
    TUYA_EXECUTE   = "tuya-execute-device"

# 场景相关主题
class SCENE_TOPIC:
	CREATE = "scene-create"
	UPDATE = "scene-update"
	DELETE = "scene-delete"
	ENABLE = "scene-enable"
	DISABLE = "scene-disable"
	REVIEW  = "scene-review"
	CHANGE  = "scene-change"

# 房子相关主题
class HOUSE_TOPIC:
    CREATE = "house-create"
    UPDATE = "house-update"
    DELETE = "house-delete"

# 房间相关主题
class ROOM_TOPIC:
    CREATE = "room-create"
    UPDATE = "room-update"
    DELETE = "room-delete"

# google智能家居平台 相关主题
class GOOGLE_SMART_HOME_TOPIC:
    REQUEST_SYNC = "smart-home-request-sync"

# 收到来自厂商云 订阅消息
class VENDOR_MESSAGE_RECEIVE_TOPIC:
    WULIAN_DATA  = "wulian-data-topic-receive"
    WULIAN_STATE = "wulian-state-topic-receive"
    WULIAN_ALARM = "wulian-alarm-topic-receive"
    WULIAN = "wulian-message-receive"
    TUYA   = "tuya-message-receive"
    EZVIZ  = "ezviz-message-receive"