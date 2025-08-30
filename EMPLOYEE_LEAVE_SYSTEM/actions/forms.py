from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.models import User
from dashboard.models import Department,LeaveType,Employees
from django.contrib.auth.hashers import make_password

class AddDepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = {'DepartmentName', 'DepartmentShortName', 'DepartmentCode' }
        
        widgets={
             'DepartmentName' : forms.TextInput(attrs={'class':'form-control'}),
             'DepartmentShortName' : forms.TextInput(attrs={'class':'form-control'}),
             'DepartmentCode' : forms.TextInput(attrs={'class':'form-control'})
   
        }
   

class AddLeaveTypeForm(ModelForm):
    class Meta:
        model = LeaveType
        fields={'LeaveType','Description'}
        
        widgets={
             'LeaveType' : forms.TextInput(attrs={'class':'form-control'}),
             'Description' : forms.TextInput(attrs={'class':'form-control'}),
           
   
        }


class EmployeeCreation(forms.ModelForm):
    class Meta:
        model = Employees
        fields = {'username','password','first_name','last_name','email','department','gender','dob','address','city','country','mobile'}
        
        widgets ={
            'username': forms.TextInput(attrs={'class':'form-control'}),
            'password': forms.PasswordInput(attrs={'class':'form-control'}),
            'first_name': forms.TextInput(attrs={'class':'form-control'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'department': forms.Select(attrs={'class':'form-control'},choices=[tuple[Department.DepartmentName]]),
            'gender': forms.Select(choices=[('',''),('Male', 'Male'), ('Female', 'Female'),('Other','Other')],attrs={'class':'form-control'}),
            'dob': forms.DateInput(attrs={'class':'form-control','type':'Date'}),
            'address': forms.TextInput(attrs={'class':'form-control'}),
            'city': forms.TextInput(attrs={'class':'form-control'}),
            'country': forms.TextInput(attrs={'class':'form-control'}),
            'mobile': forms.TextInput(attrs={'class':'form-control'}),
        }


# class EmployeeUpdationForm(forms.ModelForm):
#     class Meta:
#         model = Employees
#         fields = { 'id','username','password','first_name','last_name','email','department','gender','dob','address','city','country','mobile'}
        
#         widgets ={
#             'id' : forms.TextInput(attrs={'class' : 'form-control','value':'employee.first_name'}),
#             'username': forms.TextInput(attrs={'class':'form-control','value':'{{employee.first_name}}'}),
#             'password': forms.PasswordInput(attrs={'class':'form-control','value':'{{employee.first_name}}'}),
#             'first_name': forms.TextInput(attrs={'class':'form-control','value':'{{employee.first_name}}'}),
#             'last_name': forms.TextInput(attrs={'class':'form-control','value':'{{employee.first_name}}'}),
#             'email': forms.EmailInput(attrs={'class':'form-control','value':'{{employee.first_name}}'}),
#             'department': forms.Select(attrs={'class':'form-control','value':'{{employee.department}}'},choices=[tuple[Department.DepartmentName]]),
#             'gender': forms.Select(choices=[('',''),('Male', 'Male'), ('Female', 'Female'),('Other','Other')],attrs={'class':'form-control','value':'{{employee.first_name}}'}),
#             'dob': forms.DateInput(attrs={'class':'form-control','type':'Date','value':'{{employee.dob}}'}),
#             'address': forms.TextInput(attrs={'class':'form-control','value':'{{employee.first_name}}'}),
#             'city': forms.TextInput(attrs={'class':'form-control','value':'{{employee.first_name}}'}),
#             'country': forms.TextInput(attrs={'class':'form-control','value':'{{employee.first_name}}'}),
#             'mobile': forms.TextInput(attrs={'class':'form-control','value':'{{employee.first_name}}'}),
#         }