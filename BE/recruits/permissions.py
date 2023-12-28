from rest_framework import permissions


from teams.models import TeamMember

class IsLeaderOrReadOnly(permissions.BasePermission):
    """
    리더 권한 설정
    """
        
    def has_object_permission(self, request, view, obj):
        if request.method in ['PATCH', 'DELETE', 'PUT']:
            leader = TeamMember.objects.filter(team_id=obj.team, user=request.user.id, is_leader=True).exists()
            return request.user.is_authenticated and leader
        
        return True