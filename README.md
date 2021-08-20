## SPS_BASE

SPS CORE Base lib
- DEVICE_CATEGORY, TYPE, VENDOR
- COLLECTIONS
- DB, PUBSUB Agent

## Usage
```
pip3 install git+https://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@github.com/visionwx/sps_base.git@v1.1.33
```

## Test
```
export GCP_PROJECT=my-first-action-project-96da6
export GCP_LOCATION=us-central1
export SCENE_ACTION_TASK_QUEUE=scene-actions
export SCENE_ACTION_TASK_ENDPOINT=https://scene-kjhf45fuxq-uc.a.run.app/v1/execute-scene-action
export SCENE_ACTION_TASK_SERVICE_ACCOUNT="cloud-task@my-first-action-project-96da6.iam.gserviceaccount.com"
```

## Change
#### 2021-08-20 Update
- 【新增】新增涂鸦红外网关设备类型

#### 2021-08-10 Update
- 【新增】新增MessageType消息通知类型
- 【修复】解决tasks没有被包含到安装包的问题
- 【优化】sceneActionTask 的taskPayload增加scene_id参数

#### 2021-08-09 Update
- 【新增】新增sceneActionTask

#### 2021-08-05 Update
- 【修复】修复场景topic发布bug

#### 2021-06-22 Update
- 【新增】新增 物联wall_outlet和sound_warner设备类型

#### 2021-06-11 Update
- 【新增】新增 supportDeviceTemplatesDocument

#### 2021-06-10 Update
- 【新增】新增 smart_locker大类和设备类型
- 【新增】新增 supportDevicesCollection和supportDeviceTemplatesCollection

#### 2021-05-28 Update
- 【修复】pubsub.publisher.publishTuyaDeviceDeleteTopic 发布topic名称错误bug修复

#### 2021-05-28 Update
- 【新增】ezviz摄像头设备数据模版 nightVisionMode迁移到liveVideo, liveVideo能力更新

#### 2021-05-13 Update
- 【新增】ezviz摄像头设备数据模版 sdStorage.status改成列表 liveVideo增加分辨率支持

#### 2021-04-29 Update
- 【新增】ezviz camera设备数据模版，状态初始化

#### 2021-04-28 Update
- 【新增】ezviz camera设备数据模版，状态初始化

#### 2021-04-27 Update
- 【新增】CAMERA_W2H Template
- 【新增】发布收到涂鸦/萤石设备消息的主题函数
- 【修复】修改ezviz_message_received 主题

#### 2021-04-23 Update
- 【新增】DEVICE_TYPE toTypeId 增加新的摄像头id

#### 2021-04-21 Update
- 【修复】DEVICE_TYPE.camera_c3x内容乱码问题解决

#### 2021-04-17 Update
- 【新增】新增厂商接口异常 以及 设备验证码错误异常
- 【新增】增加物联网关数据模版
- 【优化】新增BaseException，所有exception 增加id字段

#### 2021-04-16 Update
- 【新增】新增publishTuyaDeviceDeleteTopic
- 【新增】新增publishWulianDeviceDeleteTopic，以及部分exceptions
- 【优化】去掉DeviceDocument的 vendorPrefix参数
- 【新增】新增exception，Document基类set方法增加merge参数
- 【优化】优化DeviceTemplate类，增加fromType方法

#### 2021-04-15 Update
- 【增加】auth/authorization.py新增获取用户当前房子信息函数
- 【增加】新增auth/authorization.py
- 【增加】pubsub/publisher.py新增发布设备get指令topic
- 【增加】新增萤石c3w/c3a/c3x/lc1c/bc1数据模版生成函数

#### 2021-04-13 Update
- 【优化】改成 python pacakge
- 【优化】数据库操作类优化，全部集成基类实现

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