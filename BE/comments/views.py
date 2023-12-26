from rest_framework import viewsets, status
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model

from recruits.models import RecruitmentPost
from posts.models import CommunityPost

from .models import Comment
from .serializers import CommentSerializer, CommentCreateSerializer
from .permissions import IsOwner

User = get_user_model()

class CommentPagination(PageNumberPagination):
    '''
    Pagination 커스텀
    '''
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 100

    def get_paginated_response(self, status, message, data):
        return Response({
            'status': 'success',
            'message': 'Success message',
            'count': self.page.paginator.count,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })


class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    
    def get_queryset(self):
        post_id = self.request.query_params.get('post_id')
        recruit_id = self.request.query_params.get('recruit_id')
        print(recruit_id)

        if post_id:
            return Comment.objects.filter(post_id=post_id)
        elif recruit_id:
            return Comment.objects.filter(recruit_id=recruit_id)
        else:
            return Comment.objects.all()
        
    def get_permissions(self):
        '''
        권한 설정
        '''
        if self.action == 'list':
            return [AllowAny()]
        elif self.action == 'create':
            return [IsAuthenticated()]
        elif self.action in ['update', 'partial_update', 'destroy']:
            return [IsAuthenticated(), IsOwner()]
        return super().get_permissions()
    
    def list(self, request, *args, **kwargs):
        '''
        댓글 목록 조회

        Detail:
            기존 쿼리셋에 페이지네이션 설정 후 반환
        '''
        paginator = CommentPagination()
        comments = self.get_queryset().order_by('-created_at')
        page = paginator.paginate_queryset(comments, request)
        serializer = CommentSerializer(page, many=True)
        return paginator.get_paginated_response(status='success', message='Successfully', data=serializer.data)
        
    def create(self, request, *args, **kwargs):
        self.serializer_class = CommentCreateSerializer
        data = request.data

        user_id = request.user
        post_id = data.get('post_id')
        recruit_id = data.get('recruit_id')
        content = data.get('content')
        to_user = data.get('to_user')

        comment = Comment(
            user_id = user_id,
            content = content
            )
        
        if to_user:
            to_user_instance = get_object_or_404(User, id=to_user)
            comment.to_user = to_user_instance
        if post_id:
            post_instance = get_object_or_404(CommunityPost, id=post_id)
            comment.post_id = post_instance
        elif recruit_id:
            recruit_instance = get_object_or_404(RecruitmentPost, id=recruit_id)
            comment.recruit_id = recruit_instance

        comment.save()
        return Response({'detail':'댓글이 생성되었습니다.'}, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        instance = get_object_or_404(Comment, id=kwargs.get('pk'))
        content = request.data.get('content')

        if content is not None:
            instance.content = content
            instance.save()
            return Response({'datail': '댓글이 수정되었습니다.'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': '내용이 입력되지 않았습니다.'}, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):    
        instance = get_object_or_404(Comment, id=kwargs.get('pk'))
        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)
