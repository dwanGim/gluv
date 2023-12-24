from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import CommentViewSet

router = DefaultRouter(trailing_slash=True)
router.register(r'', CommentViewSet, basename='comment')

urlpatterns = [
    path('',  include(router.urls)),
]