from django.contrib import admin
from django.urls import path, include
from drf_spectacular.views import SpectacularJSONAPIView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
    TokenVerifyView,
)
from drf_spectacular.views import (
    SpectacularAPIView, 
    SpectacularRedocView, 
    SpectacularSwaggerView
)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/books/', include("books.urls")),
    path('api/v1/chatrooms/', include("chatrooms.urls")),
    path('api/v1/comments/', include("comments.urls")),
    path('api/v1/likes/', include("likes.urls")),
    # path('api/v1/messages/', include("messages.urls")),
    path('api/v1/notifications/', include("notifications.urls")),
    path('api/v1/posts/', include("posts.urls")),
    path('api/v1/recruits/', include("recruits.urls")),
    path('api/v1/reports/', include("reports.urls")),
    path('api/v1/schedules/', include("schedules.urls")),
    path('api/v1/teams/', include("teams.urls")),
    path('api/v1/users/', include("users.urls")),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),   # 토큰발급/재생성
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),      # 토큰 검증
]

# Media url 패턴 추가
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Spectacular Document App Name
app_name = 'api'
# Spectacular Document API
urlpatterns += [
    path("docs/json/", SpectacularJSONAPIView.as_view(), name="schema-json"),
    path('schema/', SpectacularAPIView.as_view(), name='schema'),
    path('schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema-json'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='schema-json'), name='redoc'),
]
