## SPS_BASE

SPS CORE Base lib
- DEVICE_CATEGORY, TYPE, VENDOR
- COLLECTIONS
- DB, PUBSUB Agent

## Change
#### 2021-04-13 Update
- 【优化】改成 python pacakge

#### 2021-03-30 Update
- 【修复】pubsub/publisher.py WULIAN_DEVICE_CMD 导入错误修复
- 【修复】pubsub/publisher.py WULIAN_EXECUTE 变量名错误
- 【新增】db/base.py 新增Collection基类，用于抽象对数据库操作
- 【新增】db/device.py 新增 DeviceStateEventSubcriber
- 【优化】db/base.py 优化add接口，增加db/scene.py
- 【新增】db/device.py 临时新增get方法
- 【新增】pubsub/publisher.py 新增publishDeviceExecuteTopic
- 【修复】db/scene.py 修复 NAME错误
- 【优化】utils/logger.py 增加withPrint参数

#### 2021-03-29 Update
- 【新增】增加 DEVICE_ALARM.detect_scene_switch_click
- 【新增】增加 db/device.py Device.list接口
- 【新增】增加 wulian网关同步主题发布方法 以及 相关常量
- 【新增】增加 db/device.py Device.findAndUpdate接口

#### 2021-03-28 Update
- 【新增】增加场景相关常量静态类，数据库类，和事件发布类

#### 2021-03-27 Update
- 【新增】db/device_templates增加 开关类设备

#### 2021-03-26 Update
- 【修复】db/device.py DB bug修复
- 【修复】pubsub/publisher.py 更新设备状态接口bug修复
- 【修复】pubsub/publisher.py 获取日志对象接口
- 【新增】device_templates.py 新增安防检测器模版
- 【新增】device_templates.py 新增环境检测器

#### 2021-03-25 Update
- 【优化】db/device.py 发布事件时的data, 处理成完全字典
- 【优化】调整db/device.py isDeviceExists函数
- 【新增】增加device_states和device_templates
- 【优化】优化device_templates
- 【新增】增加deviceInfo,deviceHistoryAlarms,deviceHistoryDatas db类
- 【新增】deviceInfo增加get接口
- 【修复】db/device.py collections import bug fix

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