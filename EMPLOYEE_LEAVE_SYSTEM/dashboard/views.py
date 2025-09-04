from django.shortcuts import render , redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate , login ,logout
from django.contrib.auth.models import auth
import datetime 
from .models import *
from django.contrib import messages 
from .forms import *
from django.contrib.auth.decorators import login_required
from .forms import AdminLoginForm
# Create your views here.

from actions.forms import AddDepartmentForm,AddLeaveTypeForm

from django.core.paginator import Paginator

@login_required(login_url='accounts/index')
def dashboard(request):
    employee = Employees.objects.all()
    department = Department.objects.all()
    leavetype = LeaveType.objects.all()
    leaves = Leave.objects.all().order_by('Postingdate').reverse()
    data = leaves[:5]
    context ={
             'employee' : employee,
             'department' : department,
             'leavetype' : leavetype,
             'leaves'  : data,
    }
    return render(request,'accounts/dashboard.html',context)

def admin_index(request):
    form = AdminLoginForm()
    form1 = AddDepartmentForm()
    if request.method == 'POST':
        form = AdminLoginForm(request, data=request.POST)
        if form.is_valid():
             
             username = request.POST.get('username')
             password = request.POST.get('password')
             user = authenticate(request,username=username, password=password)
             if user is not None:
                 login(request, user)
                 if user.is_superuser:
                     return redirect('dashboard')
                 else:
                     messages.success(request,'invalid Details ....')
             else:
                 messages.success(request,'invalid Details ....')
       
    context ={
        'AdminLoginForm' : form,
        'form' : form1
    }
    return render(request,'accounts/index.html', context )

login_required(login_url='/')
def logoutPage(request):
    logout(request)
    return redirect('accounts/index')



def employees(request):
    emps = Employees.objects.filter(is_superuser = False)
    paginator = Paginator(emps , 3)
    page_num = request.GET.get('page')
    data = paginator.get_page(page_num)
    context = {
        'emps' : data
    }
    return render(request,'accounts/employees.html',context)


def employeeLeave_details(request,id):
    
    department = Department.objects.all()
    leavetype = LeaveType.objects.all()
    leaves = Leave.objects.get(leaveID=id)
    EmpID = leaves.user.id
    employee = Employees.objects.get(pk=EmpID)
    
    if request.method == "POST":
        leave = Leave.objects.get(leaveID=id)
        leave.Status = request.POST.get('Status')
        leave.AdminRemark = request.POST.get('Description')
        currentDate = datetime.date.today()
        formatDate = currentDate.strftime("%Y-%m-%d")
        leave.AdminRemarkDate = formatDate
        leave.save()
        messages.success(request, 'Action Applied .....')


    context ={
             'employee' : employee,
             'department' : department,
             'leavetype' : leavetype,
             'leaves'  : leaves,
    }
    return render(request,'accounts/employeeLeave-details.html',context)



def leave_section(request):
    leaves = LeaveType.objects.all()
    context = {
        'leaves' : leaves
    }
    return render(request,'accounts/leave-section.html',context)


def leave_history(request):
    employee = Employees.objects.all()
    department = Department.objects.all()
    leavetype = LeaveType.objects.all()
    leaves = Leave.objects.all().order_by('Postingdate').reverse()
    paginator = Paginator(leaves,4)
    page_num = request.GET.get('page')
    data = paginator.get_page(page_num)
      
    context ={
             'employee' : employee,
             'department' : department,
             'leavetype' : leavetype,
             'leaves'  : data
    }
    return render(request,'accounts/leave-history.html',context)

def approved_history(request):
    employee = Employees.objects.all()
    department = Department.objects.all()
    leavetype = LeaveType.objects.all()
    leaves = Leave.objects.filter(Status = 'Approved')
      
    context ={
             'employee' : employee,
             'department' : department,
             'leavetype' : leavetype,
             'leaves'  : leaves
    }
    return render(request,'accounts/approved-history.html',context)

def declined_history(request):
    employee = Employees.objects.all()
    department = Department.objects.all()
    leavetype = LeaveType.objects.all()
    leaves = Leave.objects.filter(Status = 'Declined')
      
    context ={
             'employee' : employee,
             'department' : department,
             'leavetype' : leavetype,
             'leaves'  : leaves
    }
    return render(request,'accounts/declined-history.html',context)

def pending_history(request):
    employee = Employees.objects.all()
    department = Department.objects.all()
    leavetype = LeaveType.objects.all()
    leaves = Leave.objects.filter(Status = 'Pending')
      
    context ={
             'employee' : employee,
             'department' : department,
             'leavetype' : leavetype,
             'leaves'  : leaves
    }
    return render(request,'accounts/pending-history.html',context)

def department(request):
    data = Department.objects.all()
    context={
        'data' : data
    }

    return render(request,'accounts/department.html', context)

def useradmin(request):
    data = Employees.objects.filter(is_superuser = True)
    context = {
        'data' : data
    }
    return render(request,'accounts/useradmin.html', context)
