from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views.generic import ListView, DetailView, View
from django.contrib.auth import views as auth_views
from django.views import generic
from django.urls import reverse_lazy
from .forms import LoginForm, RegisterForm
from django.contrib import messages
from django.urls import reverse


class LoginView(View):
    
    template_name="account/login.html"
    def get(self, *args, **kwargs):
        form = LoginForm()
        context = {
                'form': form
                
            }
        return render (self.request, "account/login.html", context)
    
    def post(self, *args, **kwargs):
        username = self.request.POST['username']
        password = self.request.POST['password']
        user = authenticate(self.request, username=username, password=password)
        
        if user is not None:
            login(self.request, user)
            # Redirect to a success page.
            messages.success(self.request, 'User logined')
            userfirm=self.request.user.userfirm.slug
            return redirect('dash',userfirm)
        else:
           messages.warning(self.request, 'Username or password invalid')
           return redirect('giris:login')
    

class RegisterView(View):
    
    template_name = 'account/register.html'
   

    
    def get(self, *args, **kwargs):
        form = RegisterForm()
        context = {
                'form': form
                
            }
        return render (self.request, "account/register.html", context)
    def post(self, *args, **kwargs):
              
        
        form = RegisterForm(self.request.POST or None)        
        

        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password1 = form.cleaned_data.get('password1')
            userfirm = form.cleaned_data.get('userfirm')
            password2 = form.cleaned_data.get('password2')
            
            
            form.save()
            messages.success(self.request, "registered")
            return redirect('giris:login')
        else:
           messages.warning(self.request, 'Form is not valid')
           return redirect('giris:register')






def logout_view(request):
    logout(request)
    messages.success(request, "logged out!!!!!")
    return redirect('/')        