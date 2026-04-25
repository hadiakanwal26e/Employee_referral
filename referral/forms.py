from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['employee_name', 'cnic', 'cell', 'job_title_working', 
                  'for_job', 'skill_set', 'department', 'experience_years']
        widgets = {
            'employee_name': forms.TextInput(attrs={'class': 'form-control'}),
            'cnic': forms.TextInput(attrs={'class': 'form-control'}),
            'cell': forms.TextInput(attrs={'class': 'form-control'}),
            'job_title_working': forms.TextInput(attrs={'class': 'form-control'}),
            'for_job': forms.TextInput(attrs={'class': 'form-control'}),
            'skill_set': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'department': forms.TextInput(attrs={'class': 'form-control'}),
            'experience_years': forms.NumberInput(attrs={'class': 'form-control'}),
        }