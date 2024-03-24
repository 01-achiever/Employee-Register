from django.contrib import admin
from .models import Employee
# Register your models here.

@admin.register(Employee)
class EmployyeAdmin(admin.ModelAdmin):
    list_display = ['id','Name','Position','Phone']