from django.db import models
from django.contrib.auth import get_user_model

def team_thumbnail_path(instance, filename):
    return f'team_thumbnails/team_{instance.id}/{filename}'


class Team(models.Model):
    '''
    모임 모델

    Attributes:
        category : CATEGORY_CHOICES의 선택지 중 택1
        is_closed : 모임의 모집 여부(False일 경우 모집 중)
        location : 모임이 오프라인에서 진행될 때 입력할 주소
        member : User모델과의 N:M관계 (매핑테이블 : TeamMember)

    Detail:
        모집 게시글 작성 시 같이 생성됩니다.
        location, introduce, image는 모집게시글 작성 후 팀 정보 수정에서 입력합니다.
        current_attendance == max_attendance일 경우 is_closed = false 변경 불가합니다.
    '''
    CATEGORY_CHOICES = [
        ('독서모임', '독서모임'),
        ('합평모임', '합평모임'),
        ('책집필모임', '책집필모임'),
    ]
    name = models.CharField(max_length=20, null=True, blank=True)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    is_closed = models.BooleanField(default=False)
    max_attendance = models.IntegerField()
    current_attendance=models.IntegerField(default=0)
    introduce = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=team_thumbnail_path, null=True, blank=True)
    member = models.ManyToManyField(get_user_model(), through='TeamMember', related_name='teams')

    def __str__(self):
        return self.name

class TeamMember(models.Model):
    '''
    User-Team 모델

    Attributes:
        is_leader : 해당 유저가 모임의 리더인지 구성원인지 설정
        is_approved : True일경우 모임의 구성원으로 활동 가능
    
    Detail:
        유저가 모집 게시글에서 참가 신청을 할 경우 TeamMember에 데이터가 추가됩니다.
        리더가 신청을 승인할 때 해당 유저의 is_approved의 값이 True가 되며, 모임의 구성원으로 인정됩니다.
    '''
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    is_leader = models.BooleanField(default=False)
    is_approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.team} 모임의 구성원 {self.user}'
    
    @property
    def nickname(self):
        return self.user.nickname