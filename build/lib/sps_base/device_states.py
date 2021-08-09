class HUMAN_PASS_STATE:
	HUMAN_PASS_DETECTED    = "human_pass_detected"
	NO_HUMAN_PASS_DETECTED = "no_human_pass_detected"

class SMOKE_STATE:
	SMOKE_DETECTED    = "smoke_detected"
	NO_SMOKE_DETECTED = "no_smoke_detected"

class WATER_LEAK_STATE:
	WATER_LEAK_DETECTED   = "water_leak_detected"
	NO_WATER_LEAK_DETECTED = "no_water_leak_detected"

class CONTACT_STATE:
	CONTACTOR_OPEN_DETECTED  = "contactor_open_detected"
	CONTACTOR_CLOSE_DETECTED = "contactor_close_detected"

class GAS_STATE:
	GAS_DETECTED  = "gas_detected"
	NO_GAS_DETECTED = "no_gas_detected"

# 零火开关 恢复状态设置
# 即 断电恢复之后，是否恢复断电前的状态
class RECOVER_STATE:
	DO_NOT_RECOVER = "do_not_recover_previous_state"
	RECOVER = "recover_previous_state"