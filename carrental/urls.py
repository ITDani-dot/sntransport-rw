from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('cars.urls')),  # Your cars app homepage
]

# Serve media files - uploaded car images
# This works on Render because we have MEDIA_ROOT on a Disk
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Serve static files only when DEBUG=True
# In production Render + Whitenoise handles static
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
