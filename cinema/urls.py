from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from apps.movies.views import movie_create

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('apps.settings.urls')),
    path('accounts/', include('allauth.urls')),
    path('', include('apps.users.urls')),
    path('create/', movie_create, name="create")
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)