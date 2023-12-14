from django.db import models
from django.contrib.auth import get_user_model

class Notification(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False),
    message = models.CharField(max_length=50)
    url = models.CharField(max_length=50, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.message