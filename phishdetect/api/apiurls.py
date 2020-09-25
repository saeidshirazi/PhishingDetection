from django.contrib import admin
from django.contrib.auth import views 
from django.conf.urls import url, include
from django.urls import include, path
from rest_framework import routers
from . import views
from django.conf.urls.static import static
from django.conf import settings



router = routers.DefaultRouter()
router.register(r'WhiteList', views.WhiteListViewSet,base_name='White_List')
router.register(r'BlackList', views.BlackListViewSet,base_name='Black_List')
router.register(r'Contactus', views.ContactUsViewSet,base_name='contact us')
###################################################################
import debug_toolbar

urlpatterns = [
    url("^", include(router.urls))
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
