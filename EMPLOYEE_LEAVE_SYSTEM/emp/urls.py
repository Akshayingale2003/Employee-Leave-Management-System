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
       path('', views.index, name='index'),
       path('leave',views.leave,name='leave'),
       path('my-profile',views.my_profile,name='my-profile'),
       path('my-leave-history',views.leave_history,name='my-leave-history'),
       path('change-password-employee',views.change_password_employee,name='change-password-employee'),
       path('logoutEmp',views.logoutEmp,name='logoutEmp')
]
