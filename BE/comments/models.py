from django.db import models
from django.contrib.auth import get_user_model

from posts.models import CommunityPost
from recruits.models import RecruitmentPost


class Comment(models.Model):
    '''
    자유게시글, 모집게시글의 댓글 DB

    Attributes:
        user_id : 작성자
        recruit_id : 모집게시글
        post_id : 자유게시글
        to_user : 원 댓글

    Detail:
        post_id, recruit_id 중 하나는 반드시 들어있어야 합니다.
        to_user는 자기참조합니다.
    '''
    user_id = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    recruit_id = models.ForeignKey(RecruitmentPost, on_delete=models.CASCADE, null=True, blank=True)
    post_id = models.ForeignKey(CommunityPost, on_delete=models.CASCADE, null=True, blank=True)
    content = models.TextField(max_length=100)
    to_user = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"Comment by {self.user_id}: {self.content}"

