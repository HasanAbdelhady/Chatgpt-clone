from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from chat.views import ChatView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', ChatView.as_view(), name='chat'),
    path('chat/', include('chat.urls')),
    path('users/', include('users.urls')),
    path('api/', include('rest_framework.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
