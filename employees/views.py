from django.shortcuts import render , get_object_or_404
from .models import Employee_details

# Create your views here.
def Emp_details(request,pk):
    employee_details=get_object_or_404(Employee_details,pk=pk)
    context={
            'employee':employee_details
    }
    return render(request,'employees.html',context) 