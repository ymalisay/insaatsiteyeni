from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from django.contrib import messages




class IndexView(View):
    def get(self, *args, **kwargs):
        
        context = {
          
                
            }
         
        return render(self.request, "index.html", context )


class DashView(View):
    def get(self, *args, **kwargs):
        userfirm=self.request.user.userfirm.slug   
        context = {
                'userfirm': userfirm,
                
            }
        
        return render(self.request, "index.html",context )        