from sps_base.collections import COLLECTIONS
from sps_base.pubsub.publisher import publishSceneCreateTopic
from sps_base.db.base import Collection, UserHouseCollection

# 数据库操作 用户房子 场景 集合类
class SceneCollection(UserHouseCollection):
    # 集合name字段，重写
    NAME = COLLECTIONS.scenes

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

# 即将废弃
# 数据库操作 用户房子 场景 集合类
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