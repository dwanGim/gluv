from rest_framework.routers import DefaultRouter
from django.urls import path, include

from .views import LikeViewSet

router = DefaultRouter(trailing_slash=True)
router.register(r'', LikeViewSet, basename='like')

urlpatterns = [
    path('', include(router.urls)),
]
