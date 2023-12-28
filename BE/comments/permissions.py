from rest_framework import permissions
from django.shortcuts import get_object_or_404

from .models import Comment


class IsOwner(permissions.BasePermission):
    '''
    요청한 유저가 작성자인지 확인
    '''
    def has_permission(self, request, view):
        comment_id = view.kwargs.get('pk')
        comment = get_object_or_404(Comment, id=comment_id)
        return comment.user_id == request.user or request.user.is_staff