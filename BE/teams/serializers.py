from rest_framework import serializers
from chatrooms.models import ChatRoom

from schedules.models import Schedule
from recruits.models import RecruitmentPost
from .models import Team, TeamMember


class TeamSerializer(serializers.ModelSerializer):
    '''
    Team 모델 Serializer
    '''
    class Meta:
        model = Team
        fields = ['id', 'name', 'category', 'is_closed', 'max_attendance', 'current_attendance', 'introduce', 'image']

    def to_representation(self, instance):
        ret = super().to_representation(instance)
        if not instance.image:
            ret['image'] =  '/media/defalut_team.png'
        return ret

class TeamMemberSerializer(serializers.ModelSerializer):
    '''
    TeamMember 모델 Serializer
    '''
    class Meta:
        model = TeamMember
        fields = ['user', 'nickname', 'team', 'is_leader', 'is_approved']

class TeamMemberChangeSerializer(serializers.ModelSerializer):
    '''
    TeamMember 모델 수정을 위한 Serializer
    '''
    class Meta:
        model = TeamMember
        fields = ['user']


class TeamDetailSerializer(serializers.ModelSerializer):
    '''
    Team 모델 상세 조회를 위한 Serializer
    '''
    frequency = serializers.SerializerMethodField()
    day = serializers.SerializerMethodField()
    week = serializers.SerializerMethodField()
    start_time = serializers.SerializerMethodField()
    end_time = serializers.SerializerMethodField()

    applied_member = serializers.SerializerMethodField()
    is_leader = serializers.SerializerMethodField()
    recruit_id = serializers.SerializerMethodField()
    chatroom_id = serializers.SerializerMethodField()
    location = serializers.SerializerMethodField()

    class Meta:
        model = Team
        fields = [
            'id', 'name', 'category', 'is_closed', 'location', 'max_attendance', 'current_attendance', 'introduce', 'image',
            'applied_member', 'is_leader', 'frequency', 'day', 'week', 'start_time', 'end_time', 'recruit_id', 'chatroom_id',
        ]

    def get_related_data(self, obj):
        '''
        팀 상세 조회 시 필요한 데이터 조회
        '''
        team_id = self.context.get('team_id')
        user = self.context.get('user')

        if not hasattr(obj,'related_data'):
            obj.schedule = Schedule.objects.filter(team_id=team_id).first()
            obj.is_leader = TeamMember.objects.filter(team=obj, user=user, is_leader=True).exists()
            obj.applied_member_count = TeamMember.objects.filter(team=obj, is_approved=False).count()
            obj.recruit_post = RecruitmentPost.objects.filter(team=obj).first()
            obj.chat_room = ChatRoom.objects.filter(team=obj).first()

            obj.related_data = {
                'applied_member_count': obj.applied_member_count,
                'is_leader': obj.is_leader,
                'schedule': obj.schedule,
                'recruit_post': obj.recruit_post,
                'chat_room': obj.chat_room,
            }
            
        return obj.related_data

    def get_applied_member(self, obj):
        return self.get_related_data(obj)['applied_member_count']
    
    def get_is_leader(self, obj):
        return self.get_related_data(obj)['is_leader']
    
    def get_frequency(self, obj):
        data = self.get_related_data(obj)
        return data['schedule'].frequency if data['schedule'] else None

    def get_day(self, obj):
        data = self.get_related_data(obj)
        if not data['schedule']:
            return None
        
        return data['schedule'].day if data['schedule'].day is not None else None

    def get_week(self, obj):
        data = self.get_related_data(obj)
        if not data['schedule']:
            return None
        
        return data['schedule'].week if data['schedule'].week is not None else None

    def get_start_time(self, obj):
        data = self.get_related_data(obj)
        if not data['schedule']:
            return None
        
        return data['schedule'].start_time if data['schedule'].start_time is not None else None

    def get_end_time(self, obj):
        data = self.get_related_data(obj)
        if not data['schedule']:
            return None
        
        return data['schedule'].end_time if data['schedule'].end_time is not None else None
    
    def get_recruit_id(self, obj):
        data = self.get_related_data(obj)
        if not data['recruit_post']:
            return None
        
        return data['recruit_post'].id
    
    def get_chatroom_id(self, obj):
        data = self.get_related_data(obj)
        if not data['chat_room']:
            return None
        
        return data['chat_room'].id
    
    def get_location(self, obj):
        data = self.get_related_data(obj)
        if not data['recruit_post']:
            return None
        
        return data['recruit_post'].region