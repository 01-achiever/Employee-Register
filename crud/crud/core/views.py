from django.shortcuts import render, redirect
from .forms import EmployeeForm
from .models import Employee

# Create your views here.
def employee_list(request,id):
    return render(request, "core/employee_list.html")

def employee_form(request):
    if request.method == 'POST':
       ef = EmployeeForm(request.POST)
       if ef.is_valid():
           ef.save()
       em = Employee.objects.all()
       ef = EmployeeForm()
    else:
        em = Employee.objects.all()
        ef = EmployeeForm()
    return render(request, "core/employee_form.html",{"ef":ef,"em":em})


def employee_delete(request, id):
    if request.method =='POST':
        de = Employee.objects.get(pk=id)
        de.delete()
    return redirect('employee')

def update(request,id):
    if request.method == 'POST':
        um = Employee.objects.get(pk=id)
        ef = EmployeeForm(request.POST, instance = um)
        if ef.is_valid():
            ef.save()
        ef = EmployeeForm
    else:
        um = Employee.objects.get(pk=id)
        ef = EmployeeForm(instance = um)
    return render(request,"core/employee_list.html",{"ef":ef})


