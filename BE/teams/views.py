from rest_framework.generics import get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.response import Response
from rest_framework import status
from .models import Team, TeamMember
from .serializers import TeamSerializer, TeamMemberSerializer, TeamMemberChangeSerializer, TeamDetailSerializer
from .permissions import IsLeaderOrReadOnly


class TeamListView(generics.ListAPIView):
    '''
    모임의 목록을 조회하는 View
    로그인 권한 필요
    '''
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]


class TeamDetailView(generics.RetrieveUpdateDestroyAPIView):
    '''
    모임의 상세 정보를 조회, 업데이트, 삭제하는 View
    로그인 권한 필요, 수정/삭제는 리더 권한 필요
    '''
    queryset = Team.objects.all()
    serializer_class = TeamDetailSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated, IsLeaderOrReadOnly]


class TeamJoinView(generics.UpdateAPIView):
    '''
    모임 가입 신청한 유저를 승인하기 위한 View
    로그인 권한, 리더 권한 필요
    request body : user_id (승인 대상의 user_id)
    '''
    queryset = TeamMember.objects.all()
    permission_classes = [IsAuthenticated, IsLeaderOrReadOnly]

    def update(self, request, *args, **kwargs):
        # 모임의 현재 구성원 수 증가
        team = get_object_or_404(Team, pk=self.kwargs.get('team_id'))
        if team.current_attendance >= team.max_attendance:
            return Response({'detail': '모임의 인원이 가득 찼기 때문에 더 승인할 수 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
        team.current_attendance += 1
        team.save()

        user_id = request.data.get('user_id')
        team_member = get_object_or_404(
            TeamMember, team_id=self.kwargs.get('team_id'), user_id=user_id, is_approved=False
        )
        team_member.is_approved = True
        team_member.save()

        return Response({'detail': '참가신청 승인 완료되었습니다.'}, status=status.HTTP_200_OK)
    

class TeamLeaveView(generics.DestroyAPIView):
    '''
    모임 탈퇴를 위한 View
    로그인 권한 필요
    '''
    queryset = TeamMember.objects.all()
    permission_classes = [IsAuthenticated]

    def perform_destroy(self, instance):
        # 모임 인원 수 조절
        team = get_object_or_404(Team, pk=self.kwargs.get('team_id'))
        if team.current_attendance == 1:
            return Response({'detail': '모임의 다른 구성원이 없습니다. 모임 삭제를 해주세요.'}, status=status.HTTP_400_BAD_REQUEST)
        team.current_attendance -= 1
        team.save()

        if instance.is_leader:
            # 만약 Leader인 경우, 다음 index의 유저를 Leader로 설정
            next_leader = instance.team.member.filter(is_leader=False).first()
            if next_leader:
                next_leader.is_leader = True
                next_leader.save()
        instance.delete()

        return Response({"detail": "모임 탈퇴 완료되었습니다."}, status=status.HTTP_204_NO_CONTENT)
    

class TeamKickView(generics.DestroyAPIView):
    '''
    모임의 구성원 추방을 위한 View
    로그인 권한, 리더 권한 필요
    request body : user_id (추방 대상의 user_id)
    '''
    queryset = TeamMember.objects.all()
    permission_classes = [IsAuthenticated, IsLeaderOrReadOnly]

    def get_object(self):
        user_id = self.request.data.get('user_id')
        return get_object_or_404(self.get_queryset(), user=user_id)

    def perform_destroy(self, instance):
        team = get_object_or_404(Team, pk=self.kwargs.get('team_id'))
        team.current_attendance -= 1
        team.save()
        instance.delete()
        return Response({'detail': '구성원 추방 완료되었습니다.'}, status=status.HTTP_204_NO_CONTENT)


class TeamLeaderChangeView(generics.UpdateAPIView):
    '''
    모임의 리더를 변경하기 위한 View
    로그인 권한, 리더 권한 필요
    '''
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberChangeSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated, IsLeaderOrReadOnly]

    def perform_update(self, serializer):
        previous_leader = TeamMember.objects.get(team=self.kwargs['pk'], is_leader=True)
        previous_leader.is_leader = False
        previous_leader.save()

        new_leader = TeamMember.objects.get(team=self.kwargs['pk'], user=self.request.data.get('user'))
        new_leader.is_leader = True
        new_leader.save()
        
        return Response({"detail": "리더 권한이 변경되었습니다."}, status=status.HTTP_200_OK)


class TeamMembersView(generics.ListAPIView):
    '''
    구성원 목록을 보기 위한 View
    로그인 권한 필요
    '''
    queryset = TeamMember.objects.all()
    serializer_class = TeamMemberSerializer
    permission_classes = [AllowAny]
    # permission_classes = [IsAuthenticated]

    def list(self, request, *args, **kwargs):
        queryset = self.get_queryset().filter(team_id=self.kwargs['pk'])
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)