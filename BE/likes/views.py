# views.py
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Like
from posts.models import CommunityPost
from recruits.models import RecruitmentPost
from .serializers import LikeSerializer

from rest_framework.decorators import action

class LikeViewSet(viewsets.ModelViewSet):
    '''
    좋아요를 관리하는 ViewSet입니다.
    
    - 좋아요 누르기:
      - URL: POST /api/likes/like_post/
      - 데이터: { "post_id": 1 } 또는 { "recruit_id": 1 }
      - 위의 데이터에서 1은 실제 게시물 또는 모집 게시물의 ID에 대한 것으로 대체되어야 합니다.

    - 좋아요 취소:
      - URL: POST /api/likes/unlike_post/
      - 데이터: { "post_id": 1 } 또는 { "recruit_id": 1 }

    - 내가 해당 게시물에 좋아요했는지 확인:
      - URL: GET /api/likes/is_liked/?post_id=1 또는 GET /api/likes/is_liked/?recruit_id=1
    '''
    queryset = Like.objects.all()
    serializer_class = LikeSerializer

    # 좋아요 누르기
    @action(detail=False, methods=['post'])
    def like_post(self, request):
        post_id = request.data.get('post_id')
        recruit_id = request.data.get('recruit_id')

        if not post_id and not recruit_id:
            return Response({'error': '게시글 ID가 필요합니다.'}, status=400)

        if post_id:
            post = get_object_or_404(CommunityPost, pk=post_id)
            like, created = Like.objects.get_or_create(user=request.user, community_post=post)
        elif recruit_id:
            recruit_post = get_object_or_404(RecruitmentPost, pk=recruit_id)
            like, created = Like.objects.get_or_create(user=request.user, recruitment_post=recruit_post)

        if not created:
            return Response({'error': '이미 좋아요를 눌렀습니다.'}, status=400)

        serializer = self.get_serializer(like)
        return Response(serializer.data)

    # 좋아요 취소
    @action(detail=False, methods=['post'])
    def unlike_post(self, request):
        post_id = request.data.get('post_id')
        recruit_id = request.data.get('recruit_id')

        if not post_id and not recruit_id:
            return Response({'error': '게시글 ID가 필요합니다.'}, status=400)

        
        like_query = Like.objects.filter(user=request.user)
        if post_id:
            like_query = like_query.filter(community_post__id=post_id)
        elif recruit_id:
            like_query = like_query.filter(recruitment_post__id=recruit_id)

        try:
            like = like_query.get()
        except Like.DoesNotExist:
            return Response({'error': '좋아요를 누르지 않은 게시글입니다.'}, status=400)

        like.delete()
        return Response({'message': '좋아요가 취소되었습니다.'})

    # 해당 게시물에 내가 좋아요 했는지 확인
    @action(detail=False, methods=['get'])
    def is_liked(self, request):
        post_id = request.query_params.get('post_id')
        recruit_id = request.query_params.get('recruit_id')

        if not post_id and not recruit_id:
            return Response({'error': '게시글 ID가 필요합니다.'}, status=400)

        # 해당 게시글에 대한 좋아요 찾기
        like_query = Like.objects.filter(user=request.user)
        if post_id:
            like_query = like_query.filter(community_post__id=post_id)
        elif recruit_id:
            like_query = like_query.filter(recruitment_post__id=recruit_id)

        is_liked = like_query.exists()
        return Response({'is_liked': is_liked})


