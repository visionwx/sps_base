## SPS_BASE

SPS CORE Base lib
- DEVICE_CATEGORY, TYPE, VENDOR
- COLLECTIONS
- DB, PUBSUB Agent

## Change
#### 2021-03-25 Update
- 【优化】db/device.py 发布事件时的data, 处理成完全字典
- 【优化】调整db/device.py isDeviceExists函数
- 【新增】增加device_states和device_templates

#### 2021-03-24 Update
- 【新增】增加exception 参数找不到 和 环境变量参数找不到
- 【新增】utils/parameters.py
- 【新增】wulian.py 新增 WULIAN_MQTT_SUBSCRIBE_TOPIC
- 【新增】utils/logger.py 新增日志类
- 【修复】本地包引入，增加sps_base.前缀
- 【修复】parameters.py 环境变量获取函数raiseException参数不起作用
- 【新增】pubsub/publisher.py增加物联统一消息接收事件发布函数
- 【优化】wulian.py WULIAN_MQTT_SUBSCRIBE_TOPIC优化
- 【优化】优化日志输出处理，可用环境变量配置日志输出位置
- 【新增】增加WulianMessageParameterMissingException
- 【优化】调整db/device.py对设备是否存在逻辑判断的位置

#### 2021-03-23 First commit