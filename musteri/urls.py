from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import Yenimusteri,Musteridetay, Musteriupdate, AjaxMusteriList, musteriweb_list
from rest_framework.routers import DefaultRouter


app_name = 'musteri'



urlpatterns = [
    path('yeni/', Yenimusteri.as_view(), name='yenimusteri'),
    path('ajax/musteri/', AjaxMusteriList.as_view(), name='ajaxmusteri'),
    path('liste/', musteriweb_list, name='musterilistesi'),
    path('<int:pk>/', Musteridetay.as_view(), name='musteridetay'),
    path('<int:pk>/edit', Musteriupdate.as_view(), name='musteriupdate'),
    
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
