class MessageType(Enum):
    # 设备告警
    DEVICE_ALARM = 0
    # 场景通知
    SCENE_NOTIFICATION = 1
    # 房子成员邀请
    HOUSE_MEMBER_INVITATION = 2
    # 门铃
    DOOR_BELL = 3
    # 远程开门请求
    UNLOCK_REQUEST = 4
    # 系统通知
    SYSTEM_NOTIFICATION = 5
    # 低电量通知
    LOW_BATTERY_STATE = 6