from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Notification(models.Model):
    '''
    알림 모델
    Attributes:
        user: 알림을 받을 유저
        message: 알림 메시지
        url: 알림 클릭 시 이동할 url
    '''
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)
    message = models.CharField(max_length=100)
    url = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message