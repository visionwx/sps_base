import os
import json
from google.cloud import pubsub_v1
from sps_base.exceptions import EnvironmentValueNotFoundException
from sps_base.utils.parameters import getParaFromEnvironment
from sps_base.utils.logger import getLogger
from sps_base.topics import DEVICE_TOPIC, VENDOR_MESSAGE_RECEIVE_TOPIC

TAG = "PUBLISHER"

# 获取日志实例
LOGGER = getLogger(
    logFilePath=getParaFromEnvironment(
        'log_file_path',
        defaultValue="/var/log/sps_base.log",
        raiseExceptionIfNone=False
    )
)

# 获取项目id
projectId = getParaFromEnvironment('GCP_PROJECT')

# init pubsub client
publisher = pubsub_v1.PublisherClient()

# Publish topic
def publishTopic(topicId, topicData):
    if type(topicData) == dict:
        topicData = json.dumps(topicData).encode("utf-8")
    topicPath = publisher.topic_path(projectId, topicId)
    future = publisher.publish(topicPath, topicData)
    LOGGER.info(TAG, "topicId=" + topicId 
        + ", " + str(future.result()))

# 发布设备新建/更新/删除 事件
def publishDeviceTopic(topicId, userId, houseId, 
    deviceId, deviceData):
	topicData = {
		"user_id": userId,
		"house_id": houseId,
		"device_id": deviceId,
		"device_data": deviceData
	}
	publishTopic(topicId, topicData)

# 发布设备新建 事件
def publishDeviceCreateTopic(userId, houseId, 
    deviceId, deviceData):
    publishDeviceTopic(
        DEVICE_TOPIC.CREATE, 
        userId, houseId, deviceId, 
        deviceData)

# 发布设备状态更新 事件
def publishDeviceUpdateTopic(userId, houseId, 
    deviceId, deviceData):
    publishDeviceTopic(
        DEVICE_TOPIC.UPDATE, 
        userId, houseId, deviceId, 
        deviceData)

# 发布设备删除 事件
def publishDeviceDeleteTopic(userId, houseId, 
    deviceId, deviceData=None):
    publishDeviceTopic(
        DEVICE_TOPIC.DELETE, 
        userId, houseId, deviceId, 
        deviceData)

# 发布收到物联 data  类型消息
def publishWulianDataMessageReceiveTopic(topicData):
    publishTopic(
        VENDOR_MESSAGE_RECEIVE_TOPIC.WULIAN_DATA,
        topicData
    )

# 发布收到物联 state 类型消息
def publishWulianStateMessageReceiveTopic(topicData):
    publishTopic(
        VENDOR_MESSAGE_RECEIVE_TOPIC.WULIAN_STATE,
        topicData
    )

# 发布收到物联 alarm 类型消息
def publishWulianAlarmMessageReceiveTopic(topicData):
    publishTopic(
        VENDOR_MESSAGE_RECEIVE_TOPIC.WULIAN_ALARM,
        topicData
    )

# 发布收到物联 data/state/alarm  类型消息
def publishWulianMessageReceiveTopic(topicData):
    publishTopic(
        VENDOR_MESSAGE_RECEIVE_TOPIC.WULIAN,
        topicData
    )