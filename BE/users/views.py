from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView, DeleteView
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import permissions, generics

from .serializers import UserSerializer

User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserProfileEditView(LoginRequiredMixin, UpdateView):
    model = User
    # template_name = 'user_profile_edit.html'
    fields = ['region', 'nickname', 'profile_image', 'profile_content']
    success_url = reverse_lazy('user_detail')

    def get_object(self, queryset=None):
        return self.request.user

class UserDeactivateView(LoginRequiredMixin, DeleteView):
    model = User
    # template_name = 'user_confirm_deactivate.html'
    success_url = reverse_lazy('user_deactivate')

    def get_object(self, queryset=None):
        return self.request.user
