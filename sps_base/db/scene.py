from sps_base.collections import COLLECTIONS
from sps_base.pubsub.publisher import publishSceneCreateTopic
from sps_base.db.base import Collection

class Scene(Collection):
    NAME = COLLECTIONS.scenes

    def __init__(self, userId, houseId):
        self.userId = userId
        self.houseId = houseId
        super().__init__()

    # 重写，获取设备数据库引用
    def getCollectionRef(self):
        colRef = self.DB.collection(COLLECTIONS.users
            ).document(self.userId
            ).collection(COLLECTIONS.houses
            ).document(self.houseId
            ).collection(self.NAME)
        return colRef

    # 重写，数据创建接口
    def add(self, data):
        docId = super().add(data)
        publishSceneCreateTopic(
            self.userId,
            self.houseId,
            docId,
            data
        )
        return True