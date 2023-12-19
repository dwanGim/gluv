from rest_framework import viewsets
from rest_framework.permissions import BasePermission,IsAuthenticated, AllowAny

from .models import Comment
from .serializers import CommentSerializer

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny
from .models import Comment
from .serializers import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [AllowAny()]

    # def perform_create(self, serializer):
    #     serializer.save(user=self.request.user)


# class IsCommentOwner(BasePermission):
#     def has_object_permission(self, request, view, obj):       
#         return obj.user == request.user

# class CommentViewSet(viewsets.ModelViewSet):
#     queryset = Comment.objects.all()
#     serializer_class = CommentSerializer

#     def get_permissions(self):
#         if self.action in ['create']:
#             return [IsAuthenticated()]
#         elif self.action in ['update', 'partial_update', 'destroy']:
#             return [IsAuthenticated(), IsCommentOwner()]
#         else:
#             return [AllowAny()]

#     def perform_create(self, serializer):
#         serializer.save(user=self.request.user)