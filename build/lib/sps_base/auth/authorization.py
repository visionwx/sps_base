import firebase_admin
from firebase_admin import auth
from sps_base.exceptions import UserTokenExpireException, UserTokenNotProvideException, UserNotExistException
from sps_base.db.user import UserDocument
from sps_base.utils.parameters import getParaFromDict

# cred = credentials.RefreshToken('path/to/refreshToken.json')
# default_app = firebase_admin.initialize_app(cred)
default_app = firebase_admin.initialize_app()

class User():
    currentHouse:object = None
    nickName:str = None
    avatarUrl:str = None
    
    @classmethod
    def fromDict(cls, userDataInDict):
        cls.currentHouse = getParaFromDict("current_house", userDataInDict)
        cls.nickName = getParaFromDict("nick_name", userDataInDict)
        cls.avatarUrl = getParaFromDict("avatar_url", userDataInDict, 
            raiseExceptionIfNone=False)
        return cls
    
# 从request请求的authorization获取用户id
# 判断是否授权用户
def getUserIdFromRequestHeader(request):
    authorization = request.headers.get('Authorization', None)
    if authorization is None:
        raise UserTokenNotProvideException

    idToken = authorization.replace("Bearer ", "")
    decodedToken = auth.verify_id_token(idToken)
    userId = decodedToken['uid']
    if userId is None:
        raise UserTokenExpireException()
    
    return userId

# 获取当前用户当前house的ownerId和houseId
def getUserCurrentHouseInfo(userId):
    userDoc = UserDocument(userId)
    if not userDoc.exists():
        raise UserNotExistException(userId)
    # 提取用户数据
    userData = userDoc.get()
    userObj = User.fromDict(userData)
    currentHouseOwnerId = userObj.currentHouse.get("owner_id", None)
    currentHouseId = userObj.currentHouse.get("id", None)
    return currentHouseOwnerId, currentHouseId