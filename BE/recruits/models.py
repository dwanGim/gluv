from django.db import models
from django.contrib.auth import get_user_model
from teams.models import Team

class RecruitmentPost(models.Model):
    '''
    모집 게시글 모델

    Detail:
        모집 게시글 작성에 필요한 Category와 같은 정보는 외래키로 설정한 Team 모델에서 가져옵니다.
        - Category, max_attendance, current_attendance
    '''
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    title = models.TextField()
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_count = models.IntegerField(default=0)

    def __str__(self):
        return self.title
