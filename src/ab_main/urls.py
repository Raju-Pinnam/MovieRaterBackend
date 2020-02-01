from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('admin/', admin.site.urls),
    path('users/', include(('accounts.urls', 'accounts'), namespace='account')),
    path('movies/', include(('movies.urls', 'movies'), namespace='movies')),
    path('token/', obtain_auth_token, name='token'),
    path('ratings/',include(('ratings.urls', 'ratings'), namespace='ratings'))
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
