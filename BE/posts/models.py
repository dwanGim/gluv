from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class CommunityPost(models.Model):
    '''
    커뮤니티 게시글 모델

    Attributes:
        CATEGORY_CHOICES : 커뮤니티 게시글의 카테고리를 설정
        - creation-novel/poem/essay : 자유 게시판의 하위 카테고리 소설, 시, 수필을 선택
        - comm-novel/poem/essay : 창작 게시판의 하위 카테고리 소설, 시, 수필을 선택
        is_pinned : 타 게시판의 상단에 노출될 공지사항 선택을 위한 변수
    '''
    CATEGORY_CHOICES = [
        ('notice', '공지사항'),
        ('qna', '질의/응답'),
        ('creation-novel', '창작소설'),
        ('creation-poem', '창작시'),
        ('creation-essay', '창작수필'),
        ('comm-novel', '소설'),
        ('comm-poem', '시'),
        ('comm-essay', '수필'),
    ]

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    category = models.CharField(max_length=14, choices=CATEGORY_CHOICES)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    view_count = models.IntegerField(default=0)
    is_pinned = models.BooleanField(default=False)

    def __str__(self):
        return self.title
