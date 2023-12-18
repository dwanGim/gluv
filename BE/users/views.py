from rest_framework import permissions, status
from rest_framework.views import APIView
from rest_framework.generics import CreateAPIView, RetrieveAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.mixins import UserPassesTestMixin

from .models import User
from .serializers import UserSerializer


class UserCreateView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

    def test_func(self):
        
        return not self.request.user.is_authenticated

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        
        return response

    def form_valid(self, form):
        email = form.cleaned_data.get('email')
        password1 = form.cleaned_data.get('password1')
        password2 = form.cleaned_data.get('password2')
        nickname = form.cleaned_data.get('nickname')
        
        return super().form_valid(form)

class UserDetailView(UserPassesTestMixin, RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def test_func(self):
        return self.get_object() == self.request.user

class UserProfileEditView(UserPassesTestMixin, UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def test_func(self):
        return self.get_object() == self.request.user
    

class UserDeactivateView(UserPassesTestMixin, DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def test_func(self):
        # 사용자 자신이거나 스태프 권한이 있는지 확인
        user = self.get_object()
        return user == self.request.user or self.request.user.is_staff

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()

        instance.is_active = False
        instance.save()
        response = super().destroy(request, *args, **kwargs)
       
        return response

class UserLogoutView(UserPassesTestMixin, APIView):
    permission_classes = [permissions.IsAuthenticated]

    def test_func(self):
        return self.request.user.is_authenticated and self.request.user == self.get_object()

    def post(self, request, *args, **kwargs):
        try:
            refresh_token = request.data.get('refresh', None)
            if refresh_token:
                RefreshToken(refresh_token).blacklist()

            response_data = {'detail': '성공적으로 로그아웃되었습니다.'}
            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            response_data = {'detail': '로그아웃하는 데 실패했습니다.'}
            return Response(response_data, status=status.HTTP_400_BAD_REQUEST)
        
