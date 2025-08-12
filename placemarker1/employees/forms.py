# employees/forms.py
from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['first_name', 'last_name', 'position', 'department', 'email', 'phone','hire_date']
