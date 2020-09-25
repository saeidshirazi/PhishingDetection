from django.contrib import admin
from django.contrib.auth import views 
from django.conf.urls import url, include
from rest_framework import routers
from api import apiurls,views
from django.conf.urls.static import static
from django.conf import settings
import debug_toolbar


urlpatterns = [

    url(r'^jet/', include('jet.urls', 'jet')),
    url(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    url(r'^guard/admin/', admin.site.urls),
    url(r'^checker/api/v1/', include(apiurls)),
    url(r'^__debug__/', include(debug_toolbar.urls)),
    
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

