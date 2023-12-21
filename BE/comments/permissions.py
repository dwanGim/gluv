from rest_framework import permissions
from django.shortcuts import get_object_or_404
from .models import Comment

class IsOwner(permissions.BasePermission):
    def has_permission(self, request, view):
        comment_id = view.kwargs.get('pk')
        comment = get_object_or_404(Comment, id=comment_id)
        return comment.user_id == request.user or request.user.is_staff

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user or request.user.is_staff