from rest_framework import viewsets, permissions
from rest_framework.decorators import action
from rest_framework.response import Response

from django.shortcuts import get_object_or_404

from posts.models import CommunityPost
from recruits.models import RecruitmentPost
from .models import Like
from .serializers import LikeSerializer


class LikeViewSet(viewsets.ViewSet):
    '''
    좋아요(추천)를 관리하는 ViewSet
    '''

    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        if self.action == 'like_count':
            return [permissions.AllowAny()]
        return super().get_permissions()
    
    @action(detail=False, methods=['post'])
    def like_post(self, request):
    # 좋아요 누르기
        post_id = request.data.get('post_id')
        recruit_id = request.data.get('recruit_id')

        if not post_id and not recruit_id:
            return Response({'error': '게시글 ID가 필요합니다.'}, status=400)
        if post_id and recruit_id:
            return Response({'error': '두게시물을 한번에 insert 를 할 수 없습니다.'}, status=400)

        if post_id:
            post = get_object_or_404(CommunityPost, pk=post_id)
            like, created = Like.objects.get_or_create(user=request.user, community_post=post)
        elif recruit_id:
            recruit_post = get_object_or_404(RecruitmentPost, pk=recruit_id)
            like, created = Like.objects.get_or_create(user=request.user, recruitment_post=recruit_post)

        if not created:
            return Response({'error': '이미 좋아요를 눌렀습니다.'}, status=400)

        serializer = LikeSerializer(like)
        return Response(serializer.data)

    @action(detail=False, methods=['post'])
    def unlike_post(self, request):
    # 좋아요 취소
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
            
            like.delete()
            return Response({'message': '좋아요가 취소되었습니다.'}, status=200)
        except Like.DoesNotExist:
            return Response({'message': '이미 좋아요를 누르지 않은 게시글입니다.'}, status=400)

        
       


    @action(detail=False, methods=['get'])
    def is_liked(self, request):
    # 해당 게시물에 대한 나의 좋아요 여부 확인
        post_id = request.query_params.get('post_id')
        recruit_id = request.query_params.get('recruit_id')

        if not post_id and not recruit_id:
            return Response({'error': '게시글 ID가 필요합니다.'}, status=400)

        like_query = Like.objects.filter(user=request.user)
        if post_id:
            like_query = like_query.filter(community_post__id=post_id)
        elif recruit_id:
            like_query = like_query.filter(recruitment_post__id=recruit_id)


        is_liked = like_query.exists()
        return Response({'is_liked': is_liked}, status=200)


    @action(detail=False, methods=['get'])
    def like_count(self, request):
    # 해당 게시물의 좋아요 개수 확인
        post_id = request.query_params.get('post_id')
        recruit_id = request.query_params.get('recruit_id')

        if not post_id and not recruit_id:
            return Response({'error': 'Either post_id or recruit_id is required.'}, status=400)

        try:
            post_id = int(post_id) if post_id else None
            recruit_id = int(recruit_id) if recruit_id else None
        except ValueError:
            return Response({'error': 'Invalid post_id or recruit_id.'}, status=400)

        if post_id:
            likes_count = Like.objects.filter(community_post_id=post_id).count()
        elif recruit_id:
            likes_count = Like.objects.filter(recruitment_post_id=recruit_id).count()
        else:
            return Response({'error': 'Either post_id or recruit_id is required.'}, status=400)

        return Response({'likes_count': likes_count})