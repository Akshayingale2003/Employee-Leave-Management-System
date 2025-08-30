from django.contrib import admin
from .models import *
# Register your models here.

class EmployeeAdmin(admin.ModelAdmin):

    class Meta:
        model = Employees

admin.site.register(Employees,EmployeeAdmin)

admin.site.register(Department)
admin.site.register(LeaveType)
admin.site.register(Leave)
