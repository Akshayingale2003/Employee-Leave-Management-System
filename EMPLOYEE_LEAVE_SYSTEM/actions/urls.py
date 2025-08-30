"""
URL configuration for EMPLOYEE_LEAVE_SYSTEM project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('add-employee',views.add_employee,name='add-employee'),
   path('emp/<int:id>',views.update_employee,name='update_employee'),
   path('delete_leavetype/<int:id>',views.delete_leavetype,name='delete_leavetype'),
   path('delete_department/<int:id>',views.delete_department,name='delete_department'), 
   path('dept/<int:id>',views.edit_department,name='edit-department'),
   path('lt/<int:id>',views.edit_leaveType,name='edit_leaveType'),
   path('ActEmp/<int:id>',views.Activate,name='Activate'),
   path('Inact/<int:id>',views.Inactivate,name='Inactivate'),
   path('delemp/<int:id>',views.delete_Employee,name='delete_Employee'),
   path('add-department',views.add_department,name='add-department'),
   path('add-leavetype',views.add_leavetype,name='add-leavetype'),
]
