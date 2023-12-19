from django.urls import path
from .views import TeamListView, TeamDetailView, TeamJoinView, TeamLeaveView, TeamKickView, TeamLeaderChangeView, TeamMembersView

urlpatterns = [
    path('', TeamListView.as_view(), name='team-list'),
    path('<int:pk>/', TeamDetailView.as_view(), name='team-detail'),
    path('<int:pk>/join/', TeamJoinView.as_view(), name='team-join'),
    path('<int:pk>/leave/', TeamLeaveView.as_view(), name='team-leave'),
    path('<int:pk>/kick/', TeamKickView.as_view(), name='team-kick'),
    path('<int:pk>/leader/', TeamLeaderChangeView.as_view(), name='team-leader'),
    path('<int:pk>/members/', TeamMembersView.as_view(), name='team-members'),
]