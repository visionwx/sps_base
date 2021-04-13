# 触发场景review的触发源
class SCENE_REVIEW_TRIGGER:
    # 自动场景触发：基于设备状态变化触发
    DEVICE   = "scene.trigger.DEVICE"
    # 自动场景触发：基于时间条件触发
    TIMER    = "scene.trigger.TIMER"
    # 自动场景触发：基于天气状态触发
    WEATHER  = "scene.trigger.WEATHER"
    # 自动场景触发：基于位置信息触发
    LOCATION = "scene.trigger.LOCATION"
    # 手动执行触发
    MANUAL   = "scene.trigger.MANUAL"

# 场景类型
class SCENE_TYPE:
    # 手动执行场景
    MANUALY = 0
    # 自动场景
    AUTO = 1
    # 支持的场景类型
    support_type = [0, 1]

# 场景 条件 类型
class SCENE_CONDITION_TYPE:
    # 设备状态条件
    DEVICE = "scene.rules.types.DEVICE"
    # 时间状态条件
    TIMER = "scene.rules.types.TIMER"
    # 天气状态条件
    WEATHER = "scene.rules.types.WEATHER"
    # 位置状态条件
    LOCATION = "scene.rules.types.LOCATION"

# 场景 动作 类型
class SCENE_ACTION_TYPE:
    # 执行设备指令
    EXECUTE_DEVICE = "scene.actions.types.EXECUTE_DEVICE"
    # review场景
    REVIEW_SCENE = "scene.actions.types.REVIEW_SCENE"
    # 启用/禁用场景
    ENABLE_DISABLE_SCENE = "scene.actions.types.ENABLE_DISABLE_SCENE"
    # 发送短信通知
    SEND_NOTIFICATION = "scene.actions.types.SEND_NOTIFICATION"
    # 延迟指定时间
    DELAY = "scene.actions.types.DELAY"


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