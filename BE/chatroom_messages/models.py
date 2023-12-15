from django.db import models
from django.contrib.auth import get_user_model

from chatrooms.models import ChatRoom

class ChatRoomMessage(models.Model):
    content = models.TextField()
    chatroom = models.ForeignKey(ChatRoom, on_delete=models.CASCADE)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.content}"
    