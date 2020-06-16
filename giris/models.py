from django.db import models
from django.utils import timezone
from django.conf import settings


from django.db.models import CharField, EmailField, DateTimeField, ForeignKey
from django.contrib.auth.models import AbstractUser
#Create your models here.

Usermodelchoices=[
    ('A', 'firmadmin'),
    ('S', 'standart')

]

class Firm(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    
   

class Firmuser(AbstractUser):
     
    userfirm= models.ForeignKey(Firm, on_delete=models.SET_NULL, blank=True, null=True)
    email = models.EmailField(unique=True)
    telefon = models.CharField(max_length=11)
    usermodel=CharField(max_length=1,
                  choices=Usermodelchoices,
                  default='S')
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']    

    def __str__(self):
        return self.email
