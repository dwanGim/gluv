
from django.urls import path
from .views import (
    UserCreateView,
    UserDetailView,
)

# 아직 회원가입과 유저 정보 조회만 구현
urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('<int:pk>/profile/', UserDetailView.as_view(), name='user-detail'),
]
'''
/users/login/
로그인  

/users/logout/
로그아웃

/users/signup/
회원 가입

/users/profile/
프로필 수정

/users/{user_id}/profile/
프로필 조회

/users/deactivate/
회원 탈퇴

'''