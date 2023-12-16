
from django.urls import path
from django.contrib.auth.views import LoginView
from .views import (
    UserCreateView,
    UserDetailView,

)

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'),
    path('login/', LoginView.as_view(), name='login'),
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