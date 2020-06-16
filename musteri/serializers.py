from rest_framework import serializers
from django.conf import settings
from .models import Musteri
from django.contrib.auth.models import User
from giris.models import Firm



# class Firmserializer(serializers.ModelSerializer):
#     class Meta:
#         model = Firm
#         fields = ('name',)


# class UserSerializer(serializers.ModelSerializer):
#     userfirm=Firmserializer()

#     class Meta:
       
#         model = User
#         fields = ('userfirm')

class MusteriSerializer(serializers.ModelSerializer):

   
    dog_tar= serializers.DateTimeField(read_only=True)
    created=serializers.DateTimeField(read_only=True)
    updated=serializers.DateTimeField(read_only=True)
    
    
    class Meta:
        model = Musteri
        fields = (
            'ad', 'telefon','dog_tar','created','updated'
        )

