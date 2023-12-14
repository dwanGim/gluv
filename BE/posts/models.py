from django.db import models
from django.contrib.auth import get_user_model

class CommunityPost(models.Model):
    CATEGORY_CHOICES = [
        ('notice', '공지사항'),
        ('qna', '질의/응답'),
        ('creation-novel', '소설'),
        ('creation-poem', '시'),
        ('creation-essay', '수필'),
        ('comm-novel', '소설'),
        ('comm-poem', '시'),
        ('comm-essay', '수필'),
    ]

    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.TextField()
    category = models.CharField(max_length=14, choices=CATEGORY_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_count = models.IntegerField(default=0)
    is_pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title
