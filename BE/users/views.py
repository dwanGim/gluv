# Basic Django Modules
from django.contrib.auth import get_user_model
from django.contrib.auth.views import LoginView

# Rest Framework Modules
from rest_framework import generics
from rest_framework import permissions

# Models
from .serializers import UserSerializer

User = get_user_model()

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.AllowAny]

class UserDetailView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer





