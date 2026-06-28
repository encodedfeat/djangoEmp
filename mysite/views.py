from django.shortcuts import render
from employees.models import Employee_details

def home(request):
    employee=Employee_details.objects.all()
    print(employee)
    context={
        'employee':employee
    }
    return render(request,'home.html',context)