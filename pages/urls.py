from django.urls import path, include
from django.shortcuts import render
from django.http import HttpResponse
from .views import IndexView
from django.views.generic import ListView, DetailView, View

urlpatterns = [
    
    path('', IndexView.as_view(), name='index'),
   
]
