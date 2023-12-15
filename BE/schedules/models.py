from django.db import models
from teams.models import Team


class Schedules(models.Model):
    '''
    일정 모델

    Attributes:
        team (ForeignKey): Team 모델과의 1:1 관계
        frequency : 매일, 매주, 매월과 같은 반복성을 설정합니다. 특정일만 진행할 모임일 경우 '주기없음'으로 설정합니다.
        day : 반복성 일정이 아닌 날짜를 입력할 때 사용합니다.
        week : frequency를 '매주'로 설정했을 때, 'n번째' 주를 특정하기 위해 사용합니다.
        date : 특정일을 지정합니다.
    
    Detail:
        day를 월요일, 수요일로 다중지정했을 시 DB에는 "월요일, 수요일"로 저장됩니다.
    '''
    FREQUENCY_CHOICES = [
        ('주기없음', '주기없음'),
        ('매일', '매일'),
        ('매주', '매주'),
        ('매월', '매월'),
    ]

    DAY_CHOICES = [
        ('월요일', '월요일'),
        ('화요일', '화요일'),
        ('수요일', '수요일'),
        ('목요일', '목요일'),
        ('금요일', '금요일'),
        ('토요일', '토요일'),
        ('일요일', '일요일'),
    ]
    WEEK_CHOICES = [
        (1, '첫째 주'),
        (2, '둘째 주'),
        (3, '셋째 주'),
        (4, '넷째 주'),
        (5, '다섯째 주'),
    ]

    team = models.ForeignKey(Team, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=10, choices=FREQUENCY_CHOICES)
    day = models.CharField(max_length=10, choices=DAY_CHOICES, null=True, blank=True)
    week = models.CharField(max_length=10, choices=WEEK_CHOICES, null=True, blank=True)
    date = models.DateField(null=True, blank=True)
    start_time = models.TimeField(null=True, blank=True)
    end_time = models.TimeField(null=True, blank=True)

    def __str__(self):
        return f'모임({self.team})의 일정'