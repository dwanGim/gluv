from django.urls import path

from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView,
)
from .views import (
    UserCreateView,
    UserDetailView,
    UserProfileEditView,
    UserDeactivateView,
    UserLogoutView,
)

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'), # 회원가입
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # 로그인
    path('logout/', UserLogoutView.as_view(), name='logout'), # 로그아웃
    path('<int:pk>/profile/', UserDetailView.as_view(), name='user_detail'), # 프로필
    path('<int:pk>/profile/edit/', UserProfileEditView.as_view(), name='user_profile_edit'), # 프로필 수정
    path('deactivate/', UserDeactivateView.as_view(), name='user_deactivate'), # 회원탈퇴
]
