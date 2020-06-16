from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import LoginView, RegisterView,logout_view

app_name = 'giris'

urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('register/', RegisterView.as_view(), name='register'),
    path('logout/', logout_view, name='logout')
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
