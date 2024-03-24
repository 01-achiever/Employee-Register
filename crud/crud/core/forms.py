from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['Name','Position','Phone']
        
        widgets = {
        'Name': forms.TextInput(attrs={'class': 'form-control Name'}),
        'Position': forms.TextInput(attrs={'class': 'form-control Position'}),
        'Phone': forms.TextInput(attrs={'class': 'form-control Phone'}),

        # Add more fields as needed
            }