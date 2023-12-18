# urls.py
from django.urls import path
from .views import RecruitListView, RecruitHotListView, RecruitDetailView, RecruitApplyView

urlpatterns = [
    path('', RecruitListView.as_view(), name='recruit-list'),
    path('hot/', RecruitHotListView.as_view(), name='recruit-hot-list'),
    path('<int:pk>/', RecruitDetailView.as_view(), name='recruit-detail'),
    path('<int:pk>/apply/', RecruitApplyView.as_view(), name='recruit-apply'),
]
