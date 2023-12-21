from rest_framework import serializers


from .models import RecruitmentPost
from teams.models import Team
from likes.models import Like

class RecruitmentPostSerializer(serializers.ModelSerializer):
    name = serializers.SerializerMethodField()
    likes = serializers.SerializerMethodField()
    
    class Meta:
        model = RecruitmentPost
        fields = ['id', 'team', 'author', 'title', 'content', 'region', 
                    'created_at', 'updated_at', 'view_count', 'name', 'likes']

    def get_name(self, obj):
        return obj.team.name if obj.team else None
    
    def get_likes(self, obj):
        '''
        추천수 조회
        '''
        return Like.objects.filter(recruitment_post=obj.id).count()
    
class RecruitmentPostCreateSerializer(serializers.Serializer):
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
    