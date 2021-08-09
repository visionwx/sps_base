from sps_base.db.base import Collection, Document
from sps_base.collections import COLLECTIONS

# 用户信息 文档类
class UserDocument(Document):
    # 重写集合名称
    NAME = COLLECTIONS.users

# 用户信息 集合类
class UserCollection(Collection):
    # 重写集合名称
    NAME = COLLECTIONS.users