from django import forms

from .models import Musteri
from django.db.models import CharField, EmailField, DateTimeField, ForeignKey, OneToOneField
from bootstrap_datepicker_plus import DatePickerInput




class Musteriform(forms.ModelForm):
    class Meta:
        model=Musteri
        fields = ['ad', 'telefon', 'email', 'dog_tar', 'cinsiyet', 'egitim', 'adres']
    
        widgets = {
            'dog_tar': DatePickerInput(options={
                    "format": "MM/DD/YYYY", # moment date-time format
                    "showClose": True,
                    "showClear": True,
                    "showTodayButton": True,
                }),
        }
    