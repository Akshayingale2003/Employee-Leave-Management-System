from django.shortcuts import render ,redirect ,HttpResponse
from django.contrib.auth import authenticate , login , logout
from django.contrib.auth.decorators import login_required
# Create your views here.
from dashboard.models import Employees, Leave
from .forms import EmployeeLoginForm, ApplyLeaveForm
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth.hashers import check_password , make_password
from django.contrib.auth import update_session_auth_hash

@login_required(login_url='index')
def leave(request):
     form = ApplyLeaveForm()
     employee = Employees.objects.filter(username = request.user).first()
     if request.method == "POST":
             form = ApplyLeaveForm(request.POST)
             if form.is_valid():
                  form.instance.user = employee
                  form.save()
                  messages.success(request,'Leave Applied Successsfully....     Stay Tuned for approval')

     context = {
         'ApplyLeaveForm' : form
     }
     
     return render(request,'employees/leave.html', context)


def index(request):
    if request.method == 'POST':
        form = EmployeeLoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password'] 
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                if not user.is_superuser: 
                     context = {
                         'user' : user
                     }
                     return redirect('leave')
                else:
                     messages.success(request,'invalid Details ....')
                     return redirect('index')
            else:
               messages.success(request,'invalid Details ....')
               return redirect('index')  
            
    form = EmployeeLoginForm()  
    context = {
             'form' : form
                     }    
    return render(request, 'index.html',context)

@login_required(login_url='/')
def logoutEmp(request):
    logout(request)
    return redirect('index')


def my_profile(request):
     employee = Employees.objects.filter(username = request.user).first()
     if request.method == "POST":
          employee.first_name = request.POST.get('firstName')
          employee.last_name = request.POST.get('lastName')
          employee.gender = request.POST.get('gender')
          employee.dob = request.POST.get('dob')
          employee.email = request.POST.get('email')
          employee.mobile = request.POST.get('mobile')
          employee.country = request.POST.get('country')
          employee.address = request.POST.get('address')
          employee.city = request.POST.get('city')
          employee.save()
          messages.success(request,'Your Profile Updated Successfully.....')
     context = {
          'employee' : employee
     }
     return render(request,'employees/my-profile.html',context)

def leave_history(request):
     employee = Employees.objects.filter(username = request.user).first()
     leave = Leave.objects.filter(user=employee).all()
     context = {
          'leave' : leave
     }
     return render(request,'employees/my-leave-history.html',context)

def change_password_employee(request):
     if request.method == 'POST':
        current_password = request.POST.get('oldpassword')
        new_password = request.POST.get('newpassword')
        confirm_new_password = request.POST.get('confirmpassword')

        user = authenticate(username = request.user.username, password = current_password)
        if user is not None:
            if new_password == confirm_new_password:
                user.password = new_password
                user.save()
                update_session_auth_hash(request, user)
                messages.success(request, 'Your password was successfully updated!')
            else:
                messages.error(request, "New password and confirm password didn't match.")
        else:
            messages.error(request, "Your current password is incorrect.")
     return render(request,'employees/change-password-employee.html')

