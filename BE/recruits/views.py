from rest_framework import viewsets, permissions, status
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import RecruitmentPost
from .serializers import RecruitmentPostSerializer, TeamMemberSerializer
from teams.models import Team, TeamMember
from teams.serializers import TeamSerializer, ScheduleSerializer
from schedules.models import Schedule

class RecruitmentPostViewSet(viewsets.ModelViewSet):
    '''
    모집 게시글 ViewSet

    '''
    queryset = RecruitmentPost.objects.all()
    serializer_class = RecruitmentPostSerializer
    permission_classes = [permissions.AllowAny]

    def retrieve(self, request, *args, **kwargs):
        '''
        게시글 조회 시 조회수 증가
        '''
        instance = self.get_object()
        instance.view_count += 1 
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        '''
        게시글 생성 시 Team과 Schedule 생성
        '''
        pass
    
    @action(detail=False, methods=['get'], url_path='hot', url_name='hot')
    def hot_list(self, request):
        '''
        인기 모집목록 조회 기능
        정렬 기준 : view_count
        모집 개수 : count 변수
        '''
        count = 5
        queryset = RecruitmentPost.objects.order_by('-view_count')[:count]
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=['get', 'post', 'delete'], url_path='apply', url_name='apply')
    def apply(self, request, pk=None):
        '''
        GET : 모집 게시글에 가입 신청을 넣은 유저들의 목록 반환
        POST : 로그인 한 유저가 모집게시글에 가입 신청
        DELETE : 모집게시글에 가입 신청한 유저가 신청을 취소
        '''
        post = self.get_object()
        user = request.user
        team = post.team 

        if request.method == 'GET':
            queryset = TeamMember.objects.filter(team=team, is_approved=False)
            serializer = TeamMemberSerializer(queryset, many=True)
            return Response(serializer.data)
        
        elif request.method == 'POST':
            member = TeamMember.objects.filter(user=user, team=team).exists()
            # 이미 신청한 member인지 판별
            if member:
                return Response({'detail': '이미 신청한 멤버입니다.'}, status=status.HTTP_400_BAD_REQUEST)
            data = {'user': user, 'team': team.id, 'is_leader': False, 'is_approved': False}
            serializer = TeamMemberSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({'detail': '신청이 완료되었습니다.'}, status=status.HTTP_201_CREATED)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        elif request.method == 'DELETE':
            member = TeamMember.objects.filter(user=user, team=team, is_approved=False).first()
            if not member:
                return Response({'detail': '취소할 신청이 없습니다.'}, status=status.HTTP_400_BAD_REQUEST)
            member.delete()
            return Response({'detail': '신청이 취소되었습니다.'}, status=status.HTTP_200_OK)
