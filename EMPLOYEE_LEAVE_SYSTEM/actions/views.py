from django.shortcuts import render , redirect
from dashboard.models import *
from .forms import AddDepartmentForm, AddLeaveTypeForm, EmployeeCreation
from django.contrib import messages
# Create your views here.
from django.contrib.auth.hashers import make_password, check_password


def add_employee(request):
    form = EmployeeCreation()
    if request.method == "POST":
        form = EmployeeCreation(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'New Employee Added Successfully.....')
    dept = Department.objects.all()
    context={
        'dept' : dept,
        'EmployeeCreation' : form,
    }
    return render(request,'accounts/add-employee.html',context)

def add_leavetype(request):
    form = AddLeaveTypeForm()
    if request.method == "POST" :
        form = AddLeaveTypeForm(request.POST)
        form.save()
        messages.success(request,'New Leave Type Added Successfully....')
        return redirect('/add-leavetype')
    context = {
        'AddLeaveTypeForm' : form
      }
    return render(request,'accounts/add-leavetype.html',context)

def add_department(request):
    form = AddDepartmentForm()
    if request.method == 'POST':
        form = AddDepartmentForm(request.POST)
        form.save()
        messages.success(request,'New Department Added Successfully....')
        return redirect('/add-department')
    
    context={
        'AddDepartmentForm' : form
        }

    return render(request,'accounts/add-department.html',context)



def edit_leaveType(request,id):
    leavetype = LeaveType.objects.get(pk=id)
    if request.method == "POST":
        leavetype.LeaveType = request.POST.get('leavetype')
        leavetype.Description = request.POST.get('description')
        leavetype.save()
        messages.success(request, "LeaveType Edited Successfully....")
    context={
           'leavetype' : leavetype
       }   
    return render(request,'accounts/edit-leaveType.html',context)



def edit_department(request,id): 
    department = Department.objects.get(pk=id)
    if request.method == "POST":
       department.DepartmentName = request.POST.get('departmentName')
       department.DepartmentShortName = request.POST.get('departmentShortName')
       department.DepartmentCode = request.POST.get('departmentCode')
       department.save()
       messages.success(request,"Department Edited Successfully....")
    context={
           'department' : department
       }   
    return render(request,'accounts/edit-department.html',context)



def delete_department(request,id):
     department = Department.objects.get(pk=id)
     department.delete()
     messages.success(request,'Department Deleted Successfully....')
     return redirect('department')


def delete_leavetype(request,id):
     leaveType = LeaveType.objects.get(pk=id)
     leaveType.delete()
     messages.success(request,'Leave Type Deleted Successfully....')
     return redirect('leave-section')



def update_employee(request,id):
    employee = Employees.objects.get(id=id)
    department = Department.objects.all()
    password = check_password(request,employee.password)
    if request.method =="POST":
        employee.first_name = request.POST.get('firstName')
        employee.last_name = request.POST.get('lastName')
        employee.email = request.POST.get('email')
        employee.gender = request.POST.get('gender')
        employee.mobile = request.POST.get('mobile')
        employee.country = request.POST.get('country')
        employee.address = request.POST.get('address')
        employee.city  = request.POST.get('city')
        employee.password = request.POST.get('password')
        employee.save()
        messages.success(request, 'Employee Updated Successfully ......')
    context={
           'employee' : employee,
           'department': department,
           'password' : password
       }   
    return render(request,'accounts/update-employee.html',context)


def Activate(request,id):
    emp = Employees.objects.get(pk=id)
    emp.status = 'Active'
    emp.save()
    messages.success(request,"Employee Activated Successfully....")
    return redirect('employees')

def Inactivate(request,id):
    emp = Employees.objects.get(pk=id)
    emp.status = 'Inactive'
    emp.save()
    messages.success(request,"Employee Inactivated Successfully....")
    return redirect('employees')

def delete_Employee(request,id):
    emp = Employees.objects.get(pk=id)
    emp.delete()
    messages.success(request,'Employee Deleted Successfully....')
    return redirect('employees')
