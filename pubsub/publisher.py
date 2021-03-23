import os
import json
from google.cloud import pubsub_v1
from exceptions import EnvironmentValueNotFoundException
from utils import logger
from topics import DEVICE_TOPIC, VENDOR_MESSAGE_RECEIVE_TOPIC

TAG = "PUBLISHER"

# environment value
projectId = os.environ.get('GCP_PROJECT', None)
if projectId is None:
    raise EnvironmentValueNotFoundException('GCP_PROJECT')

# init pubsub client
publisher = pubsub_v1.PublisherClient()

# Publish topic
def publishTopic(topicId, topicData):
    if type(topicData) == dict:
        topicData = json.dumps(topicData).encode("utf-8")
    topicPath = publisher.topic_path(projectId, topicId)
    future = publisher.publish(topicPath, topicData)
    logger.info(TAG, "topicId=" + topicId 
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