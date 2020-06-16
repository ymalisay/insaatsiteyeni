from django import forms
from .models import Firm, Firmuser

from django.contrib.auth import (
    authenticate,
    get_user_model,

)
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User = get_user_model()


class RegisterForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('email', 'username', 'password1', 'password2', 'userfirm')


class LoginForm(AuthenticationForm):
    username = forms.CharField(label='Email / Username')
    