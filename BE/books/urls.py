from django.urls import path, include
from rest_framework.routers import DefaultRouter

from books.views import RecentBookView

router = DefaultRouter(trailing_slash=True)
router.register(r'', RecentBookView, basename='books')

urlpatterns = [
    path('',  include(router.urls)),
]
