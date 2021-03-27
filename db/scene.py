from sps_base.collections import COLLECTIONS
from google.cloud import firestore
from sps_base.pubsub.publisher import publishSceneCreateTopic

class Scene:
    # init firestore object
    DB = firestore.Client()

    def __init__(self, userId, houseId):
        self.userId = userId
        self.houseId = houseId
        self.collectionRef = self.getCollectionRef()

    # 获取设备数据库引用
    def getCollectionRef(self):
        colRef = self.DB.collection(COLLECTIONS.users
            ).document(self.userId
            ).collection(COLLECTIONS.houses
            ).document(self.houseId
            ).collection(COLLECTIONS.scenes)

        return colRef

    # 数据创建接口 封装
    def add(self, data):
        _,docRef = self.collectionRef.add(data)
        publishSceneCreateTopic(
            self.userId,
            self.houseId,
            docRef.id,
            data
        )
        return True
    
    # 获取数据
    def get(self, sceneId):
        sceneDataObj = self.collectionRef.document(
            sceneId).get()
        if sceneDataObj.exists:
            return None
        return sceneDataObj.to_dict()

    def list(self):
        pass
    
    # 数据更新接口 封装
    def update(self, data):
        pass
    
    # 数据删除接口 封装
    def delete(self):
        pass