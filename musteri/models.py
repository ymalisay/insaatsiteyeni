from django.db import models
from django.conf import settings
from django.shortcuts import reverse
from django.db.models import CharField, EmailField, DateTimeField, ForeignKey, OneToOneField




# Create your models here.

CINSIYET_CHOICES=[
        ('K', 'Kadın'),
        ('E', 'Erkek'),
        ('D', 'Diğer'),]

EGITIM_CHOICES=[
        ('I', 'İlkokul'),
        ('O', 'Ortaokul'),
        ('L', 'Lise'),
        ('M', 'Önlisans'),
        ('U', 'Lisans'),
    ]

class Musteri(models.Model):

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    ad = models.CharField(max_length=50, blank=True, null=True)
    telefon = models.CharField(max_length=11, blank=True, null=True) 
    email= models.EmailField(max_length=254, blank=True, null=True)
    dog_tar= models.DateField(blank=True, null=True)
    created=models.DateTimeField(auto_now_add=True,blank=True, null=True )
    updated=models.DateTimeField(auto_now=True,blank=True, null=True)
    
    cinsiyet=models.CharField(max_length=1, choices=CINSIYET_CHOICES,blank=True, null=True ) 
    
    egitim=(CharField(max_length=1, choices=EGITIM_CHOICES,blank=True, null=True ) )
    adres=models.TextField(max_length=254,blank=True, null=True)

    def __str__(self):
        return self.ad
   
    def get_absolute_url(self):
         return reverse("musteri:yenimusteri", kwargs={'slug': self.user.userfirm.slug})    
   
            