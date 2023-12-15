from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include("main.urls")),
    # path('chatrooms/', include("chatrooms.urls")),
    # path('comments/', include("comments.urls")),
    # path('likes/', include("likes.urls")),
    # path('messages/', include("messages.urls")),
    # path('notifications/', include("notifications.urls")),
    # path('posts/', include("posts.urls")),
    # path('recruits/', include("recruits.urls")),
    # path('reports/', include("reports.urls")),
    # path('schedules/', include("schedules.urls")),
    # path('teams/', include("teams.urls")),
    # path('users/', include("users.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)