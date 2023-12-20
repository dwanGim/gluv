from rest_framework import serializers
from .models import RecruitmentPost
from teams.serializers import ScheduleSerializer


class RecruitmentPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = RecruitmentPost
        fields = ['id', 'team', 'author', 'title', 'content', 'region', 'created_at', 'updated_at', 'view_count']


class RecruitmentPostCreateSerializer(serializers.ModelSerializer):
    frequency = serializers.CharField(source='team.schedule.frequency')
    week = serializers.ListField(child=serializers.CharField(), source='team.schedule.week')
    day = serializers.ListField(child=serializers.CharField(), source='team.schedule.day')

    category = serializers.CharField(source='team.category')
    max_attendance = serializers.IntegerField(source='team.max_attendance')

    class Meta:
        model = RecruitmentPost
        fields = ['id', 'team', 'author', 'title', 'content', 'region', 'created_at', 'updated_at', 'view_count', 'frequency', 'week', 'day', 'category', 'max_attendance']
