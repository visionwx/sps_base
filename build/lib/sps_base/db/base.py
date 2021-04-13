import abc
from google.cloud import firestore

# 数据库操作基类
class Collection(metaclass=abc.ABCMeta):
    # 集合名称
    NAME = None
    # 集合引用
    REF = None
    # init firestore object
    DB = firestore.Client()

    def __init__(self):
        self.REF = self.getCollectionRef()
    
    @abc.abstractmethod
    def getCollectionRef(self):
        pass

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