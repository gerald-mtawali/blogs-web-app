from django import forms
from django.contrib.auth.models import User 
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForm(UserCreationForm): 
    email = forms.EmailField()
    
    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'ModelName'
        verbose_name_plural = 'ModelNames'
        model=User
        fields = ['username', 'email', 'password1', 'password2']