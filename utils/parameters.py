import os
from sps_base.exceptions import ParametersNotProvideException, EnvironmentValueNotFoundException

# 从一个字典 提取 参数
def getParaFromDict(fieldName, dataInDict, 
	defaultValue=None, raiseExceptionIfNone=True):
    fieldValue = dataInDict.get(fieldName, defaultValue)
    if fieldValue is None and raiseExceptionIfNone:
        raise ParametersNotProvideException(fieldName)
    return fieldValue

# 从环境变量 提取 参数
def getParaFromEnvironment(fieldName, 
	defaultValue=None, raiseExceptionIfNone=True):
    fieldValue = os.environ.get(fieldName, defaultValue)
    if fieldValue is None:
        raise EnvironmentValueNotFoundException(fieldName)
    return fieldValue