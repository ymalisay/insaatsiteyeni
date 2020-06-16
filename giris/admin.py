# Register your models here.
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import AbstractUser

from .models import Firm, Firmuser


class FirmAdmin(admin.ModelAdmin):

    list_display = [
    'name', 
    'slug', 
    'created_at', 
    'updated_at']


class FirmuserAdmin(UserAdmin):
    
    
    list_display = [
    'email',
    'username',
    'userfirm',
    'usermodel', 
    'first_name',
    'last_name',
    'date_joined'  
    ]
    
    

admin.site.register(Firm)
admin.site.register(Firmuser, FirmuserAdmin)