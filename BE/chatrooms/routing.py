from django.urls import path
from . import consumers

websocket_urlpatterns = [
    path("v1/chatrooms/<int:room_id>/", consumers.ChatRoomConsumer.as_asgi()),
]
