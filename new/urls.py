from django.contrib import admin
from django.urls import include, path
from django.conf import settings
from django.conf.urls.static import static

admin.site.site_header = "Admin Dashboard"
admin.site.site_title = "Students Counseling Portal Admin"
admin.site.index_title = "Welcome to Students Counseling Portal Admin"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),  # Include the home app's URLs
]

#  Serve media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
