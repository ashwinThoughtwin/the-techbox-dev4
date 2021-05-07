from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [

	path('',include('homeblog.urls')),
    path('',include('account.urls')),
    path('',include('dashboard.urls')),
    path('admin/', admin.site.urls),
    path('api/auth/', include('rest_framework.urls')),
    path('api-token-auth/', obtain_auth_token, name='api_token_auth'),
    
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, 
document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, 
document_root=settings.MEDIA_ROOT)