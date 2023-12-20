from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Comment
from .serializers import CommentSerializer, CommentCreateSerializer ,CommentUpdateSerializer, CommentDeleteSerializer

class CommentViewSet(viewsets.ModelViewSet):
    serializer_class = CommentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        post_id = self.request.query_params.get('post_id')
        recruit_id = self.request.query_params.get('recruit_id')

        if post_id:
            return Comment.objects.filter(post_id=post_id)
        elif recruit_id:
            return Comment.objects.filter(recruit_id=recruit_id)
        else:
            return Comment.objects.all()

    def perform_create(self, serializer):
        # 댓글 생성
        serializer = CommentCreateSerializer(data=self.request.data, context={'request': self.request})
        serializer.is_valid(raise_exception=True)
        serializer.save(user_id=self.request.user)  

    def update(self, request, *args, **kwargs):
        # 댓글 수정
        instance = self.get_object()
        serializer = CommentUpdateSerializer(instance, data=request.data, partial=True, context={'request': request})
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

    def destroy(self, request, *args, **kwargs):
        # 댓글 삭제
        serializer = CommentDeleteSerializer(data={'comment_id': kwargs['pk']}, context={'request': request})
        serializer.is_valid(raise_exception=True)

        instance = self.get_object()
        self.check_object_permissions(request, instance)
        self.perform_destroy(instance)

        return Response(status=status.HTTP_204_NO_CONTENT)
