
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "My Portfolio"
admin.site.index_title = "Welcome to My Portfolio Admin Panel"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/portfolio/', include('my_app.urls')),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
