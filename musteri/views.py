from django.shortcuts import render, get_object_or_404
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from rest_framework import viewsets
from .serializers import MusteriSerializer
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Q
from django.core.serializers.json import DjangoJSONEncoder
from django.contrib.auth import get_user_model

from django.db.models.functions import Lower
from .forms import Musteriform
from django.contrib import messages
from django.urls import reverse
from .models import Musteri
import json
import re
# Create your views here.
User = get_user_model()

class Yenimusteri(View):
    #template_name="musteri/yenimusteri"
    def get(self, *args, **kwargs):
        userfirm=self.request.user.userfirm.slug
        
        form = Musteriform()
        context = {
                'form': form,
                'userfirm':userfirm,
                
             
                
            }
        return render (self.request, "musteri/yenimusteri.html", context)
    def post(self, *args, **kwargs):
           
        userfirm=self.request.user.userfirm.slug
       
        form = Musteriform(self.request.POST or None)
        context = {
                             
                'form': form,
                'userfirm':userfirm,
              
           
              
             
            }       
        
        

        if form.is_valid():
            musteri=Musteri() 
                       
            musteri.ad = form.cleaned_data.get('ad')
            musteri.telefon = form.cleaned_data.get('telefon')
            musteri.user=self.request.user     
            musteri.save() 
            pk=musteri.pk 
            messages.success(self.request, "Yeni Müşteri Kaydedildi")
            return redirect('musteri:musteridetay', userfirm, pk)
        else:
           messages.warning(self.request, 'Form is not valid')
           return redirect('musteri:yenimusteri', context)


class Musteridetay(View):
    #template_name="musteri/yenimusteri"
    def get(self, *args, **kwargs):
        userfirm=self.request.user.userfirm.slug
        
        musteri=Musteri.objects.get(pk=self.kwargs.get('pk'))
    
        context = {
                'musteri': musteri,
                'userfirm':userfirm,
             'pk':musteri.pk,
                
            }
        return render (self.request, "musteri/musteridetay.html", context)        

    

class AjaxMusteriList(View):
    serializer_class = MusteriSerializer
        
    def post(self, request, userfirm):
        musteris = self._datatables(request, userfirm)
        userfirm=self.request.user.userfirm.slug 
        print(musteris,)
        return HttpResponse(json.dumps(musteris, cls=DjangoJSONEncoder), content_type='application/json')
        
    def _datatables(self, request, userfirm):
        
        datatables = request.POST
        userfirm=self.request.user.userfirm.slug 
        # Ambil draw
        draw = int(datatables.get('draw'))
        # Ambil start
        start = int(datatables.get('start'))
        # Ambil length (limit)
        length = int(datatables.get('length'))
        # Ambil data search
        search = datatables.get('search[value]')
        order_idx = int(datatables.get('order[0][column]'))
        order_dir = datatables.get('order[0][dir]')
        order_col = 'columns[' + str(order_idx) + '][data]'
        order_col_name = datatables.get(order_col)
        # Set record total
        if not self.request.user.is_superuser:
            records_total = Musteri.objects.filter(user__userfirm=self.request.user.userfirm).exclude().count()
        else:
            records_total = Musteri.objects.all().count()
        # Set records filtered
        records_filtered = records_total
        # Ambil semua invoice yang valid
        if not self.request.user.is_superuser:
            musteris = Musteri.objects.filter(user__userfirm=self.request.user.userfirm)
        else:
            musteris = Musteri.objects.all()
            
        if search:
            musteri2=Musteri.objects.filter(user__userfirm=self.request.user.userfirm)
            musteris = musteri2.filter(
                    Q(ad__icontains=search)|
                    Q(telefon__icontains=search)|
                    Q(email__icontains=search)).exclude().order_by(Lower('ad'))
            records_total = musteris.count()
            records_filtered = records_total

        # Atur paginator
        
    
    
       

        if (order_dir == "desc"):
            order_col_name =  str('-' + order_col_name)
            
            
            idx=0
            for itemcol in datatables:
                colname = 'columns['+str(idx)+'][data]'
                                            
                colname = datatables.get(colname)
                                           
                idx+=1
                
                musteris = musteris.order_by(order_col_name, 'pk')
        
        else:
                          
                musteris = musteris.order_by(order_col_name, 'pk')        

   
        paginator = Paginator(musteris, length)

        page_number = start / length + 1

        try:
            object_list = paginator.page(page_number).object_list
        except PageNotAnInteger:
            object_list = paginator.page(1).object_list
        except EmptyPage:
            object_list = paginator.page(1).object_list

        userfirm=request.user.userfirm.slug
        data = [
            {
            
                'id':inv.id,
                'ad': inv.ad,
                'telefon': inv.telefon,
                'email': inv.email,
                'dog_tar': inv.dog_tar,
                'cinsiyet': inv.cinsiyet,
                'egitim': inv.egitim,
                'adres': inv.adres,
                'created': inv.created,
                'updated':inv.updated,
                'userfirm':userfirm
                
            } for inv in object_list
            ]
        
        return {
            'draw': draw,
            'recordsTotal': records_total,
            'recordsFiltered': records_filtered,
            'data': data,
            'userfirm': userfirm,
        }
   
def musteriweb_list(request, userfirm):
    userfirm=request.user.userfirm.slug
  
    
    data_context = { 'userfirm':userfirm,}
    return render(request, 'musteri/musterilist.html', data_context )


class Musteriupdate(View):
    #template_name="musteri/musteriupdate"
    def get(self, *args, **kwargs):
        userfirm=self.request.user.userfirm.slug

        musteri=Musteri.objects.get(pk=self.kwargs.get('pk'))
        
        
        form = Musteriform(instance=musteri)
        context = {
                'form': form,
                'userfirm':userfirm,
                'musteri': musteri,
                'pk':musteri.pk 
              
                            }
        
       
        
        
        return render (self.request, "musteri/musteriupdate.html", context)
    def post(self, *args, **kwargs):
        musteri=Musteri.objects.get(pk=self.kwargs.get('pk'))      
        userfirm=self.request.user.userfirm.slug
        pk=musteri.pk 
        form = Musteriform(self.request.POST or None, instance=musteri)
        context = {
                             
                'form': form,
                'userfirm':userfirm,
                'musteri': musteri,
                'pk':musteri.pk 
              
             
            }       
        
        

        if form.is_valid():
            musteri=Musteri.objects.get(pk=self.kwargs.get('pk'))
            musteri.ad = form.cleaned_data.get('ad')
            musteri.telefon = form.cleaned_data.get('telefon')
            musteri.email = form.cleaned_data.get('email')
            musteri.dog_tar = form.cleaned_data.get('dog_tar')
            musteri.user=self.request.user     
            musteri.save() 
           
            messages.success(self.request, "Müşteri bilgileri Güncellendi")
            return redirect('musteri:musteridetay', userfirm, pk)
        else:
           messages.warning(self.request, 'Form is not valid')
           return redirect('musteri:musteriupdate', userfirm, pk)
