import os
import json
from google.cloud import pubsub_v1
from sps_base.exceptions import EnvironmentValueNotFoundException
from sps_base.utils.parameters import getParaFromEnvironment
from sps_base.utils.logger import getLogger
from sps_base.topics import DEVICE_TOPIC, VENDOR_MESSAGE_RECEIVE_TOPIC, SCENE_TOPIC
from sps_base.devices import WULIAN_DEVICE_CMD, EXECUTE_DEVICE_TRIGGER

TAG = "PUBLISHER"

# 获取日志实例
LOGGER = getLogger(
    logToConsole=getParaFromEnvironment(
        'log_to_console',
        defaultValue=False,
        raiseExceptionIfNone=False
    ),
    logFilePath=getParaFromEnvironment(
        'log_file_path',
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
        DEVICE_TOPIC.STATE_UPDATE, 
        userId, houseId, deviceId, 
        deviceData)

# 发布设备删除 事件
def publishDeviceDeleteTopic(userId, houseId, 
    deviceId, deviceData=None):
    publishDeviceTopic(
        DEVICE_TOPIC.DELETE, 
        userId, houseId, deviceId, 
        deviceData)

# 发布执行设备指令 事件
def publishDeviceExecuteTopic(userId, houseId, 
    deviceId, executions, trigger, triggerData):
    topicId = DEVICE_TOPIC.EXECUTE
    topicData = {
        "user_id": userId,
        "house_id": houseId,
        "device_id": deviceId,
        "executions": executions,
        "trigger": trigger,
        "trigger_data": triggerData
    }
    publishTopic(topicId, topicData)

# 由 场景review触发 的 设备指令执行 事件发布
def publishDeviceExecuteTopicBySceneReview(userId, houseId, 
    deviceId, executions, sceneId):
    trigger = EXECUTE_DEVICE_TRIGGER.SCENE
    triggerData = {
        "scene_id": sceneId
    }
    publishDeviceExecuteTopic(userId, houseId, 
        deviceId, executions, trigger, triggerData)

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

# 发布物联gw同步消息
def publishWulianDeviceSyncTopic(wulianUserId, wulianGwDeviceId):
    topicData = {
        "command_type": WULIAN_DEVICE_CMD.SYNC,
        "command_para": {
            "wulian_user_id": wulianUserId,
            "wulian_gw_device_id": wulianGwDeviceId
        }
    }
    publishTopic(
        DEVICE_TOPIC.WULIAN_EXECUTE, 
        topicData
    )

# 发布物联device get指令消息
def publishWulianDeviceGetTopic(wulianUserId, wulianGwDeviceId):
    topicData = {
        "command_type": WULIAN_DEVICE_CMD.GET,
        "command_para": {
            "wulian_user_id": wulianUserId,
            "wulian_gw_device_id": wulianGwDeviceId
        }
    }
    publishTopic(
        DEVICE_TOPIC.WULIAN_EXECUTE, 
        topicData
    )

# 发布物联device delete指令消息
def publishWulianDeviceDeleteTopic(wulianUserId, 
    wulianGwDeviceId, wulianDeviceId, wulianDeviceType):
    topicData = {
        "command_type": WULIAN_DEVICE_CMD.DELETE_DEVICE,
        "command_para": {
            "wulian_user_id": wulianUserId,
            "wulian_gw_device_id": wulianGwDeviceId,
            "wulian_device_id": wulianDeviceId,
			"wulian_device_type": wulianDeviceType
        }
    }
    publishTopic(
        DEVICE_TOPIC.WULIAN_EXECUTE, 
        topicData
    )

# 发布场景相关事件
def publishSceneTopic(topicId, userId, houseId, 
    sceneId, sceneData, 
    trigger=None, triggerData=None):
    topicData = {
        "user_id": userId,
        "house_id": houseId,
        "scene_id": sceneId,
        "scene_data": sceneData,
        "trigger": trigger,
        "trigger_data": triggerData
    }
    publishTopic(topicId, topicData)

def publishSceneReviewTopic(userId, houseId, 
    sceneId, sceneData, 
    trigger=None, triggerData=None):
    topicId = SCENE_TOPIC.REVIEW
    publishSceneTopic(userId, houseId, 
        sceneId, sceneData, 
        trigger, triggerData)

# CHANGE == create or update or delete
def publishSceneChangeTopic(userId, houseId, 
    sceneId, sceneData, 
    trigger=None, triggerData=None):
    topicId = SCENE_TOPIC.CHANGE
    publishSceneTopic(userId, houseId, 
        sceneId, sceneData, 
        trigger, triggerData)

def publishSceneCreateTopic(userId, houseId, 
    sceneId, sceneData, 
    trigger=None, triggerData=None):
    topicId = SCENE_TOPIC.CREATE
    publishSceneTopic(userId, houseId, 
        sceneId, sceneData, 
        trigger, triggerData)
    # 同时发布change事件
    publishSceneChangeTopic(userId, houseId, 
        sceneId, sceneData, 
        trigger, triggerData)

def publishSceneUpdateTopic(userId, houseId, 
    sceneId, sceneData, 
    trigger=None, triggerData=None):
    topicId = SCENE_TOPIC.UPDATE
    publishSceneTopic(userId, houseId, 
        sceneId, sceneData, 
        trigger, triggerData)
    # 同时发布change事件
    publishSceneChangeTopic(userId, houseId, 
        sceneId, sceneData, 
        trigger, triggerData)

def publishSceneDeleteTopic(userId, houseId, 
    sceneId, sceneData, 
    trigger=None, triggerData=None):
    topicId = SCENE_TOPIC.DELETE
    publishSceneTopic(userId, houseId, 
        sceneId, sceneData, 
        trigger, triggerData)
    # 同时发布change事件
    publishSceneChangeTopic(userId, houseId, 
        sceneId, sceneData, 
        trigger, triggerData)

def publishSceneEnableTopic(userId, houseId, 
    sceneId, sceneData, 
    trigger=None, triggerData=None):
    topicId = SCENE_TOPIC.ENABLE
    publishSceneTopic(userId, houseId, 
        sceneId, sceneData, 
        trigger, triggerData)

def publishSceneDisableTopic(userId, houseId, 
    sceneId, sceneData, 
    trigger=None, triggerData=None):
    topicId = SCENE_TOPIC.DISABLE
    publishSceneTopic(userId, houseId, 
        sceneId, sceneData, 
        trigger, triggerData)
