import os
import json
from google.cloud import pubsub_v1
from exceptions import EnvironmentValueNotFoundException
from utils import logger
from topics import DEVICE_TOPIC

TAG = "PUBLISHER"

# environment value
projectId = os.environ.get('GCP_PROJECT', None)
if projectId is None:
    raise EnvironmentValueNotFoundException('GCP_PROJECT')

# init pubsub client
publisher = pubsub_v1.PublisherClient()

# Publish topic
def publishTopic(topicId, topicDataInDict):
    topicDataEncode = json.dumps(topicDataInDict).encode("utf-8")
    topicPath = publisher.topic_path(projectId, topicId)
    future = publisher.publish(topicPath, topicDataEncode)
    logger.info(TAG, "topicId=" + topicId 
        + ", " + str(future.result()))

def publishDeviceTopic(topicId, userId, houseId, 
    deviceId, deviceData):
	topicData = {
		"user_id": userId,
		"house_id": houseId,
		"device_id": deviceId,
		"device_data": deviceData
	}
	publishTopic(topicId, topicData)

def publishDeviceCreateTopic(userId, houseId, 
    deviceId, deviceData):
    publishDeviceTopic(
        DEVICE_TOPIC.CREATE, 
        userId, houseId, deviceId, 
        deviceData)

def publishDeviceUpdateTopic(userId, houseId, 
    deviceId, deviceData):
    publishDeviceTopic(
        DEVICE_TOPIC.UPDATE, 
        userId, houseId, deviceId, 
        deviceData)

def publishDeviceDeleteTopic(userId, houseId, 
    deviceId, deviceData=None):
    publishDeviceTopic(
        DEVICE_TOPIC.DELETE, 
        userId, houseId, deviceId, 
        deviceData)