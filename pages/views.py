from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from django.contrib import messages




# Create your views here.

def index(request, user):
    context=dict()
    context['user']=user
    return render(request, 'index.html', context)


def login(request):
    return render(request, 'login.html', {})

def login2(request):
    return render(request, 'login2.html', {})

class IndexView(View):
    def get(self, *args, **kwargs):
        
        return render(self.request, "index.html")