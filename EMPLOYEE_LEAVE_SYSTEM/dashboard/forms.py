from django import forms
from django.contrib.auth.forms import UserCreationForm , AuthenticationForm
from django.contrib.auth.models import User
from .models import Employees

# class EmployeeForm(UserCreationForm):
#     class Meta(UserCreationForm.Meta):
#         model = Employees
        
class AdminLoginForm(AuthenticationForm):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


