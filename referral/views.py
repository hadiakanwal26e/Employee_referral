from django.shortcuts import render, redirect
from .models import Employee
from .forms import EmployeeForm

def showAll(request):
    employees = Employee.objects.all()
    return render(request, 'showAll.html', {'employees': employees})

def insertEmployee(request):
    form = EmployeeForm()
    if request.method == 'POST':
        form = EmployeeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showAll')
    return render(request, 'insertForm.html', {'form': form})

def deleteEmployee(request):
    id = request.GET['id']
    employee = Employee.objects.get(id=id)
    employee.delete()
    return redirect('showAll')

def updateEmployee(request):
    id = request.GET['id']
    employee = Employee.objects.get(id=id)
    form = EmployeeForm(instance=employee)
    if request.method == 'POST':
        form = EmployeeForm(request.POST, instance=employee)
        if form.is_valid():
            form.save()
            return redirect('showAll')
    return render(request, 'updateForm.html', {'form': form})