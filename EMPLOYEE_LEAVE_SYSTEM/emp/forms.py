from django import forms
from django.contrib.auth.forms import AuthenticationForm
from dashboard.models import Leave , LeaveType


class EmployeeLoginForm(forms.Form):
    username = forms.CharField(label='Username')
    password = forms.CharField(label='Password', widget=forms.PasswordInput)


class ApplyLeaveForm(forms.ModelForm):
    class Meta:
        model = Leave
        fields = {'LeaveType', 'ToDate','FromDate', 'Description' }

        widgets = {
            'LeaveType' : forms.Select(attrs={'class':'form-control'},choices=[tuple[LeaveType.LeaveType]]),
            'ToDate' : forms.DateInput(attrs={'class':'form-control','type':'Date'}),
            'FromDate' : forms.DateInput(attrs={'class':'form-control','type':'Date'}),
            'Description' : forms.Textarea(attrs={'class':'form-control'}),
        }


