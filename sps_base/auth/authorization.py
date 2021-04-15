import firebase_admin
from firebase_admin import auth
from sps_base.exceptions import UserTokenExpireException, UserTokenNotProvideException

# cred = credentials.RefreshToken('path/to/refreshToken.json')
# default_app = firebase_admin.initialize_app(cred)
default_app = firebase_admin.initialize_app()

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