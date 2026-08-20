from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cars.urls')), # your home page urls
]

# Serve media files in development AND production
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# For production on Render when DEBUG=False
urlpatterns += [
    path('media/<path:path>/', serve, {'document_root': settings.MEDIA_ROOT}),
]