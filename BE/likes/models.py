from django.db import models
from django.contrib.auth import get_user_model

from posts.models import CommunityPost
from recruits.models import RecruitmentPost


class Like(models.Model):
    '''
    좋아요 모델

    Attributes:
        community_post(ForeignKey): CommunityPost 모델과의 1:M관계
        recruitment_post(ForeignKey): RecruitmentPost 모델과의 1:M관계
    
    Detail:
        좋아요 모델은 유저가 커뮤니티게시글 or 모집게시글에서 좋아요 버튼을 눌렀을 때 사용됩니다.
        커뮤니티게시글에서 좋아요를 눌렀을 때 recruitment_post는 null으로 발송됩니다.
    '''
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    community_post = models.ForeignKey(CommunityPost, on_delete=models.CASCADE, null=True, blank=True)
    recruitment_post = models.ForeignKey(RecruitmentPost, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f'{self.user}가 누른 Like'
