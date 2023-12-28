from django.urls import path, include
from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter(trailing_slash=True)
router.register(r'', views.ChatRoomListView, basename='chatroom_list')

urlpatterns = [
    path('',  include(router.urls)),
]
