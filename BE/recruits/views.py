from rest_framework import generics, permissions
from rest_framework.permissions import AllowAny
from .models import RecruitmentPost
from .serializers import RecruitmentPostSerializer
from teams.models import Team

'''
조회수 : Like 모델에서 filter 후 count
'''
class RecruitListView(generics.ListCreateAPIView):
    queryset = RecruitmentPost.objects.all()
    serializer_class = RecruitmentPostSerializer
    permission_classes = [permissions.IsAuthenticated]

class RecruitHotListView(generics.ListAPIView):
    queryset = RecruitmentPost.objects.order_by('-view_count')[:5]
    serializer_class = RecruitmentPostSerializer
    # permission_classes = [permissions.IsAuthenticated]
    permission_classes = [AllowAny]

class RecruitDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = RecruitmentPost.objects.all()
    serializer_class = RecruitmentPostSerializer
    permission_classes = [permissions.IsAuthenticated]

class RecruitApplyView(generics.CreateAPIView):
    queryset = RecruitmentPost.objects.all()
    serializer_class = RecruitmentPostSerializer
    permission_classes = [permissions.IsAuthenticated]