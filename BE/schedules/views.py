from django.shortcuts import get_object_or_404
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework import pagination
from rest_framework.permissions import IsAuthenticated, AllowAny, IsAdminUser, BasePermission
from rest_framework import status
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiParameter

from notifications.models import Notification
from teams.models import TeamMember
from .serializers import ChangeScheduleSerializer, ScheduleSerializer
from .models import Schedule


@extend_schema_view(
    change=extend_schema(
        responses={status.HTTP_200_OK: ScheduleSerializer(many=False)},
        request=ChangeScheduleSerializer(),
    )

)
class ScheduleView(viewsets.ViewSet):
    '''
    스케줄 관련 ViewSet
    '''

    def get_permissions(self):
        return [IsAuthenticated()]
    
    def generate_response(self, status, message, data=None):
        return {
            'status': status,
            'message': message,
            'data': data,
        }
    def check_team_leader_permission(self, user, team, schedule):
        is_team_leader = TeamMember.objects.filter(
            user=user, 
            team=team, 
            is_leader=True, 
            is_approved=True
        ).exists()
        return is_team_leader
    
    @action(methods=["patch"], detail=True, url_path='', url_name="change")
    def change(self, request, *args, **kwargs):
        '''
        일정 변경 API
        '''
        schedule_id = kwargs.get('pk')
        schedule = get_object_or_404(Schedule, id=schedule_id)
        
        # 현재 유저가 해당 일정의 팀의 팀장인지 확인
        if not self.check_team_leader_permission(request.user, schedule.team, schedule):
            response = self.generate_response(
                status='error',
                message='일정을 변경할 권한이 없습니다.',
                data=None
            )
            return Response(status=status.HTTP_403_FORBIDDEN, data=response)
        
        # 파라미터가 맞는 지 확인
        serializer = ChangeScheduleSerializer(instance=schedule, data=request.data)
        if not serializer.is_valid():
            response = self.generate_response(
                status='error',
                message='일정 변경에 실패하였습니다.',
                data=serializer.errors
            )
            return Response(status=status.HTTP_400_BAD_REQUEST, data=response)
                
        serializer.save()
        # 팀 멤버 전체를 대상으로 알림 생성
        team_members = TeamMember.objects.filter(team=schedule.team, is_approved=True)
        for member in team_members:
            Notification.objects.create(
                user=member.user,
                message=f"{schedule} 일정이 변경되었습니다: ",
            )

        # generate_response를 이용하여 리턴
        response_data = ScheduleSerializer(schedule).data
        response = self.generate_response(
            status='success',
            message='일정이 성공적으로 변경되었습니다.',
            data=response_data
        )
        return Response(status=status.HTTP_200_OK, data=response)