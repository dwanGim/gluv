from rest_framework import serializers

from likes.models import Like
from schedules.models import Schedule
from teams.models import Team

from .models import RecruitmentPost


class RecruitmentPostSerializer(serializers.ModelSerializer):
    '''
    모집게시글 조회를 위한 시리얼라이저
    '''
    name = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    schedule_id = serializers.SerializerMethodField()
    
    class Meta:
        model = RecruitmentPost
        fields = ['id', 'team', 'author', 'title', 'content', 'region', 
            'created_at', 'updated_at', 'view_count', 'name', 'likes', 'schedule_id']

    def get_name(self, obj):
        return obj.team.name if obj.team else None
    
    def get_likes(self, obj):
        '''
        추천수 조회
        '''
        return Like.objects.filter(recruitment_post=obj.id).count()
    
    def get_schedule_id(self, obj):
        '''
        일정이 있다면 일정 ID 반환
        '''
        schedules = Schedule.objects.filter(team=obj.team)
        if schedules.exists():
            return schedules.first().id
        
        return None
    
class RecruitmentPostCreateSerializer(serializers.Serializer):
    '''
    모집게시글 생성을 위한 시리얼라이저
    '''
    # 게시글 필수 파라미터
    title = serializers.CharField(required=True)
    content = serializers.CharField(required=True)
    # 게시글 옵션 파라미터
    region = serializers.CharField(required=False)
    # 팀 모델 관련 필수 파라미터
    category = serializers.CharField(required=True)
    max_attendance = serializers.IntegerField(required=True)
    # 팀 지정 옵션 파라미터
    team_id = serializers.IntegerField(required=False)
    # 일정 모델 관련 옵션 파라미터
    frequency = serializers.CharField(required=False)
    week = serializers.CharField(required=False)
    day = serializers.CharField(required=False)

    # 읽기 전용 
    team = serializers.SerializerMethodField()

    def get_team(self, obj):
        if self.validated_data is None:
            return None
        team_id = self.validated_data.get('team_id')
        
        try: 
            return Team.objects.get(id=team_id)
        except Exception as e:
            return None
    