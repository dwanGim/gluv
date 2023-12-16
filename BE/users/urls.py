from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated

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
)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def user_logout(request):
    try:
        # 현재 사용자의 refresh 토큰을 무효화
        refresh_token = request.data.get('refresh', None)
        if refresh_token:
            RefreshToken(refresh_token).blacklist()

        response_data = {'detail': 'Successfully logged out.'}
        return Response(response_data, status=200)
    except Exception as e:
        response_data = {'detail': 'Failed to log out.'}
        return Response(response_data, status=400)

urlpatterns = [
    path('signup/', UserCreateView.as_view(), name='signup'), # 회원가입
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'), # 로그인
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'), # 토큰발급/재생성
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'), # 토큰 검증
    path('logout/', user_logout, name='logout'), # 로그아웃
    path('<int:pk>/profile/', UserDetailView.as_view(), name='user_detail'), # 프로필
    path('<int:pk>/profile/edit/', UserProfileEditView.as_view(), name='user_profile_edit'), # 프로필 수정
    path('deactivate/', UserDeactivateView.as_view(), name='user_deactivate'), # 회원탈퇴
]
