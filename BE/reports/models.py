from django.db import models
from django.contrib.auth import get_user_model

class Report(models.Model):
    reported_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reported_user')
    reporting_user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='reporting_user')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'신고자 : {self.reporting_user}, 대상 : {self.reported_user}'