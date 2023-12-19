from rest_framework import serializers
from .models import RecruitmentPost
from teams.models import TeamMember

class RecruitmentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentPost
        fields = ['id', 'team', 'author', 'title', 'content', 'created_at', 'updated_at', 'view_count']

class TeamMemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['user', 'team', 'is_leader', 'is_approved']