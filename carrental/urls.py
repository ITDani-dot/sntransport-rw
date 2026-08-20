from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cars.urls')),  # Your cars app homepage
]

# Serve MEDIA files - uploaded car images
# This must be OUTSIDE the DEBUG if statement for Render
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve STATIC files only when DEBUG=True
# On Render production, WhiteNoise handles static
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
