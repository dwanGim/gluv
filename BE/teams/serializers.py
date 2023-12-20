from rest_framework import serializers
from schedules.models import Schedule
from django.contrib.auth import get_user_model
from .models import Team, TeamMember

class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = ['name', 'category', 'is_closed', 'location', 'max_attendance', 'current_attendance', 'introduce', 'image', 'member']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['id', 'email', 'nickname', 'profile_image']


class TeamMemberSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = TeamMember
        fields = ['user', 'is_leader', 'is_approved']


class TeamMemberChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TeamMember
        fields = ['user', 'team', 'is_leader', 'is_approved']
        # fields = ['user', 'team', 'is_leader']

class ScheduleSerializer(serializers.ModelSerializer):
    day = serializers.ListField(child=serializers.CharField(), allow_empty=True)
    week = serializers.ListField(child=serializers.CharField(), allow_empty=True)

    class Meta:
        model = Schedule
        fields = ['frequency', 'day', 'week', 'start_time', 'end_time']

class TeamDetailSerializer(serializers.ModelSerializer):
    schedule = ScheduleSerializer()

    class Meta:
        model = Team
        fields = ['name', 'category', 'is_closed', 'location', 'max_attendance', 'current_attendance', 'introduce', 'image', 'schedule']
    
    def update(self, instance, validated_data):
        schedule_data = validated_data.pop('schedule', {})
        schedule_instance = instance.schedule

        # schedule 데이터 업데이트
        for key, value in schedule_data.items():
            setattr(schedule_instance, key, value)

        # 유효성 검사를 통한 데이터 저장
        schedule_serializer = ScheduleSerializer(instance=schedule_instance, data=schedule_data)
        schedule_serializer.is_valid(raise_exception=True)
        schedule_serializer.save()

        # Team 모델의 나머지 필드 업데이트
        for key, value in validated_data.items():
            setattr(instance, key, value)
            
        instance.save()

        return instance