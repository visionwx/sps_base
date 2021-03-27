class SCENE_REVIEW_TRIGGER:
    # auto
    DEVICE   = "scene.trigger.DEVICE"
    TIMER    = "scene.trigger.TIMER"
    WEATHER  = "scene.trigger.WEATHER"
    LOCATION = "scene.trigger.LOCATION"
    # manually
    MANUAL   = "scene.trigger.MANUAL"

class SCENE_TYPE:
    MANUALY = 0
    AUTO = 1
    support_type = [0, 1]

class SCENE_CONDITION_TYPE:
    DEVICE = "scene.rules.types.DEVICE"
    TIMER = "scene.rules.types.TIMER"
    WEATHER = "scene.rules.types.WEATHER"
    LOCATION = "scene.rules.types.LOCATION"

class SCENE_ACTION_TYPE:
    EXECUTE_DEVICE = "scene.actions.types.EXECUTE_DEVICE"
    REVIEW_SCENE = "scene.actions.types.REVIEW_SCENE"
    ENABLE_DISABLE_SCENE = "scene.actions.types.ENABLE_DISABLE_SCENE"
    SEND_NOTIFICATION = "scene.actions.types.SEND_NOTIFICATION"
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