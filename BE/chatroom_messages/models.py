from django.db import models
from django.contrib.auth import get_user_model

from chatrooms.models import ChatRoom

User = get_user_model()


class ChatRoomMessage(models.Model):
    content = models.TextField()
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content}"
    