import datetime
import json
import time
import uuid
from sps_base.utils.parameters import getParaFromEnvironment
from sps_base.db.base import Collection
from google.cloud import tasks_v2
from google.protobuf import timestamp_pb2

# project = 'my-first-action-project-96da6'
# queue = 'state-delay-update'
# location = 'us-central1'
# url = 'https://us-central1-my-first-action-project-96da6.cloudfunctions.net/send_email_code'
# payload = {"email_address": "samdychen2013@outlook.com"}
# service_account_email = "cloud-task@my-first-action-project-96da6.iam.gserviceaccount.com"
# task_name = "projects/" + project + "/locations/" + location + "/queues/" + queue + "/tasks/" + str(uuid.uuid1())

# 获取项目id
# PROJECT_ID = getParaFromEnvironment(
#     'GCP_PROJECT')
# PROJECT_LOCATION = getParaFromEnvironment(
#     'GCP_LOCATION')
# SCENE_ACTION_TASK_QUEUE = getParaFromEnvironment(
#     'SCENE_ACTION_TASK_QUEUE')
# SCENE_ACTION_TASK_ENDPOINT = getParaFromEnvironment(
#     'SCENE_ACTION_TASK_ENDPOINT')
# SCENE_ACTION_TASK_SERVICE_ACCOUNT = getParaFromEnvironment(
#     'SCENE_ACTION_TASK_SERVICE_ACCOUNT')

class HttpTask:
    projectId = None
    projectLocation = None
    taskServiceAccount = None
    taskQueue = None
    taskEndpoint = None
    taskPayload = None
    inSeconds = None

    def __init__(self, 
        taskPayload,
        inSeconds,
        taskQueue,
        taskEndpoint,
        taskServiceAccount=None,
        projectId=None,
        projectLocation=None
    ):
        self.projectId = projectId
        if self.projectId is None:
            self.projectId = getParaFromEnvironment(
                'GCP_PROJECT')
        self.projectLocation = projectLocation
        if self.projectLocation is None:
            self.projectLocation = getParaFromEnvironment(
                'GCP_LOCATION')
        self.taskServiceAccount = taskServiceAccount
        self.taskQueue = taskQueue
        self.taskEndpoint = taskEndpoint
        self.taskPayload = taskPayload
        self.inSeconds = inSeconds
        self.taskName = self.composeTaskId(
            taskId=str(uuid.uuid1()))
        # Create a client.
        self.taskClient = tasks_v2.CloudTasksClient()

    def composeTaskId(self, taskId):
        return (
            "projects/" + 
            self.projectId + 
            "/locations/" + 
            self.projectLocation + 
            "/queues/" + 
            self.taskQueue + 
            "/tasks/" + 
            taskId
        )
    
    def composeTaskRequest(self):
        # Construct the request body.
        task = {
            "http_request": {  # Specify the type of request.
                "http_method": tasks_v2.HttpMethod.POST,
                "url": self.taskEndpoint,
                # "oidc_token": {
                #     "service_account_email": self.taskServiceAccount
                # },
            }
        }

        if self.taskPayload is not None:
            if isinstance(self.taskPayload, dict):
                # Convert dict to JSON string
                payload = json.dumps(self.taskPayload).encode()
                # specify http content-type to application/json
                task["http_request"]["headers"] = {
                    "Content-type": "application/json"
                }
            # Add the payload to the request.
            task["http_request"]["body"] = payload

        if self.inSeconds is not None:
            # Convert "seconds from now" into an rfc3339 datetime string.
            d = datetime.datetime.utcnow() + datetime.timedelta(
                seconds=self.inSeconds)
            # Create Timestamp protobuf.
            timestamp = timestamp_pb2.Timestamp()
            timestamp.FromDatetime(d)
            # Add the timestamp to the tasks.
            task["schedule_time"] = timestamp

        if self.taskName is not None:
            # Add the name to tasks.
            task["name"] = self.taskName
        
        return task

    def create(self):
        # Construct the fully qualified queue name.
        parent = self.taskClient.queue_path(
            self.projectId, 
            self.projectLocation, 
            self.taskQueue
        )
        # Use the client to build and send the task.
        response = self.taskClient.create_task(
            request={
                "parent": parent, 
                "task": self.composeTaskRequest()
            }
        )
        print("Created task {}".format(response.name))
        return response

class SceneActionTask(HttpTask):
    def __init__(self,  
        sceneId, 
        sceneActionList, 
        inSeconds,
        taskQueue=None,
        taskEndpoint=None,
        taskServiceAccount=None,
        projectId=None,
        projectLocation=None
    ):
        self.sceneId = sceneId
        self.sceneActionList = sceneActionList
        self.taskPayload = {
            "scene_action_list": sceneActionList,
            "scene_id": sceneId,
        }
        if taskQueue is None:
            taskQueue = getParaFromEnvironment(
                'SCENE_ACTION_TASK_QUEUE')
        if taskEndpoint is None:
            taskEndpoint = getParaFromEnvironment(
                'SCENE_ACTION_TASK_ENDPOINT')
        if taskServiceAccount is None:
            taskServiceAccount = getParaFromEnvironment(
                'SCENE_ACTION_TASK_SERVICE_ACCOUNT',
                raiseExceptionIfNone=False
            )
        super().__init__(
            taskPayload=self.taskPayload,
            inSeconds=inSeconds,
            taskQueue=taskQueue,
            taskEndpoint=taskEndpoint,
            taskServiceAccount=taskServiceAccount,
            projectId=projectId,
            projectLocation=projectLocation
        )
    
    def create(self):
        resp = super().create()
        SceneActionTaskCollection().add({
            "taskId": self.taskName,
            "sceneId": self.sceneId,
            "sceneActions": self.sceneActionList,
            "inSeconds": self.inSeconds,
            "createTime": time.time() * 1000,
        })
        return resp
        
class SceneActionTaskCollection(Collection):
    NAME = "sceneActionTasks"


# create task queue
# gcloud tasks queues create scene-actions
# gcloud tasks queues describe scene-actions

def delayAction(seconds):
    return {
        "type": "scene.actions.types.DELAY",
        "data": {
            "seconds": seconds
        }
    }
def executeDeviceAction():
    return {
        "type": "scene.actions.types.EXECUTE_DEVICE",
        "data": {
            "name": "switch switch_1",
            "description": "switch switch_1",
            "user_id": "",
            "house_id": "",
            "device_id": "",
            "executions": [
                {
                    "command": "action.devices.commands.SwitchToggles",
                    "params": {
                        "currentToggleSettings": {
                            "switch1": False
                        }
                    }
                }
            ]
        }
    }

def testSceneActionTask():
    sceneActionList = [
        executeDeviceAction(),
        delayAction(10),
        executeDeviceAction()
    ]
    resp = SceneActionTask(
        sceneId="1111",
        sceneActionList=sceneActionList,
        inSeconds=30
    ).create()