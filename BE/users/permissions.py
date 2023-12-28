from rest_framework.permissions import BasePermission


class IsOwner(BasePermission):
    '''
    객체의 소유자인지 확인
    '''
    def has_object_permission(self, request, view, obj):
        return obj == request.user