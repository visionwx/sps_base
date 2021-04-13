import abc
from google.cloud import firestore
from sps_base.collections import COLLECTIONS

# 数据库操作 集合基类
class Collection(metaclass=abc.ABCMeta):
    # 集合名称
    NAME = None
    # 集合引用
    REF = None
    # init firestore object
    DB = firestore.Client()

    def __init__(self):
        self.REF = self.getCollectionRef()
    
    def getCollectionRef(self):
        colRef = self.DB.collection(self.NAME)
        return colRef

    # 把字典格式的 condition 转换成 三元组
    def parseCondition(self, condition):
        if type(condition) is not dict:
            return None,None,None

        for fieldName in condition.keys():
            for op,fieldValue in condition[fieldName].items():
                return fieldName,op,fieldValue

        return None,None,None

    def add(self, data):
        _,docRef = self.REF.add(data)
        return docRef.id
    
    def delete(self, documentId):
        return self.REF.document(
            documentId).delete()
    
    def update(self, documentId, data):
        return self.REF.document(
            documentId).update(data)
    
    # 获取单条记录
    def get(self, documentId):
        docRef = self.REF.document(
            documentId)
        if not docRef.get().exists:
            return None
        return docRef.get().to_dict()
    
    # 条件查询获取
    def list(self, condition = None):
        fieldName, op, fieldValue = self.parseCondition(
            condition)

        if fieldName is not None:
            return map(
                lambda item:item.to_dict(), 
                self.REF.where(
                    fieldName, op, fieldValue).stream()
            )
        
        return map(
            lambda item:item.to_dict(), 
            self.REF.stream()
        )
    
    # 查找并更新
    def findAndUpdate(self, updateData, 
        condition = None):
        fieldName, op, fieldValue = self.parseCondition(
            condition)

        stream = None
        if fieldName is not None:
            stream = self.REF.where(
                    fieldName, op, fieldValue).stream()
        else:
            stream = self.REF.stream()
        
        for perDoc in stream:
            perDoc.reference.update(updateData)

# 数据库操作 文档基类
class Document(metaclass=abc.ABCMeta):
    # 集合名称
    NAME = None
    # 文档id
    ID = None
    # 文档引用
    REF = None
    # init firestore object
    DB = firestore.Client()
    # 字段列表
    FIELDS = []
    REQUIRED_FIELDS = []

    def __init__(self, docId):
        self.ID = docId
        self.REF = self.getDocumentRef()
    
    def getDocumentRef(self):
        docRef = self.DB.collection(self.NAME
            ).document(self.ID)
        return docRef
    
    # 文档是否存在
    def exists(self):
        return self.REF.get().exists

    # 创建文档
    def create(self, data):
        # 数据检查
        # 执行操作
        return self.REF.create(data)

    # 创建或者覆盖文档
    def set(self, data):
        return self.REF.set(data)

    # 更新文档
    def update(self, data):
        return self.REF.update(data)

    # 删除文档
    def delete(self):
        return self.REF.delete()

    # 获取文档, 返回字典或者none
    def get(self):
        if not self.exists():
            return None
        return self.REF.get().to_dict()

# 数据库操作 用户房子下的集合基类
# users --> houses --> 在这个路径下的集合
class UserHouseCollection(Collection):
    def __init__(self, userId, houseId):
        self.userId = userId
        self.houseId = houseId
        super().__init__()
    
    # 获取数据表集合应用，重写
    def getCollectionRef(self):
        colRef = self.DB.collection(COLLECTIONS.users
            ).document(self.userId
            ).collection(COLLECTIONS.houses
            ).document(self.houseId
            ).collection(self.NAME
            )
        return colRef