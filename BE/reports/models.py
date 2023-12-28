from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Report(models.Model):
    '''
    신고 모델
    
    Attribute:
        reported_user : 신고 대상
        reporting_user : 신고자
        content : 신고 내용
        created_at : 신고 날짜
    Detail:
        신고 버튼을 눌렀을 때, 신고자가 상세한 내용을 입력하도록 하고, 신고 대상이 되는 유저의 id를 받아와서 저장
    '''
    reported_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reported_user')
    reporting_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reporting_user')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'신고자 : {self.reporting_user}, 대상 : {self.reported_user}'