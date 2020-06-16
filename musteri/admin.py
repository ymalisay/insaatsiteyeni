from django.contrib import admin

# Register your models here.
from .models import Musteri



class MusteriAdmin(admin.ModelAdmin):

    list_display = [
        'ad', 
        'telefon', 
        'user' 
        ]

    list_display_links = [
        'ad', 
        'telefon', 
        'user' 
        ]

admin.site.register(Musteri, MusteriAdmin)
