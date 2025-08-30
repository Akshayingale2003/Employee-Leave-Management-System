from django.db import models
from django.contrib.auth.models import AbstractUser
import datetime
# Create your models here.

# class User(AbstractUser):
    

class Department(models.Model):
    DepartmentID = models.IntegerField(auto_created=True, primary_key=True, serialize=True)
    DepartmentName = models.CharField(max_length=50, null= False)
    DepartmentShortName = models.CharField(max_length=5)
    DepartmentCode = models.CharField(max_length=10)
    currentDate = datetime.date.today()
    formatDate = currentDate.strftime("%Y-%m-%d")
    CreationDate = models.DateField(default=formatDate,null=True)

    def __str__(self):
        return self.DepartmentName
    
class Employees(AbstractUser):
     is_Employee = models.BooleanField(default=True)
     status = models.CharField(max_length=50,choices=(('Active','Active'),('Inactive','Inactive'),),default='Active', null=True)
     gender = models.CharField(max_length=50,null=True)
     dob = models.DateField(null=True)
     department = models.ForeignKey(Department,null=True,on_delete=models.SET_NULL)
     address = models.CharField(max_length=50, null=True)
     city = models.CharField(max_length=50, null=True)
     country = models.CharField(max_length=50, null=True)
     mobile = models.CharField(max_length=13, null=True)
     
     def save(self, *args, **kwargs):
        # Encrypt the password before saving
        if self.password:
            self.set_password(self.password)
        
        super(Employees, self).save(*args, **kwargs)
    

     def __str__(self):
        return self.username
     

class LeaveType(models.Model):
    LeaveID = models.IntegerField(auto_created=True, primary_key=True, serialize=True)
    LeaveType =models.CharField(max_length=50 , null = False)
    Description =models.CharField(max_length=200 , null = True)
    currentDate = datetime.date.today()
    formatDate = currentDate.strftime("%Y-%m-%d")
    CreationDate =models.DateField(default=formatDate,null=True)

    def __str__(self):
        return self.LeaveType


class Leave(models.Model):
    leaveID = models.IntegerField(auto_created=True, serialize=True, primary_key=True)
    LeaveType = models.ForeignKey(LeaveType, on_delete = models.SET_NULL, null=True)
    ToDate = models.DateField()
    FromDate = models.DateField()
    Description = models.CharField(max_length=200)
    currentDate = datetime.date.today()
    formatDate = currentDate.strftime("%Y-%m-%d")
    Postingdate = models.DateField(default=formatDate,null=True)
    AdminRemark = models.CharField(max_length=100 , null=True)
    AdminRemarkDate = models.DateField(null=True)
    Status = models.CharField(max_length=50,choices=(('Approved','Approved'),('Declined','Declined'),('Pending','Pending')),default='Pending',null = True)
    user = models.ForeignKey(Employees,on_delete=models.CASCADE, null = True)
    
    def __str__(self):
        return str(self.leaveID)


