from django.http import request
from django.shortcuts import render
from .models import student
from .froms import studentregistration
# Create your views here.

def showfromdata(request):
    fm = studentregistration(auto_id = True,initial = {'name':'abid'})
    # fm.order_fields(field_order=['name','email','student_Id'])
    return render(request, 'enroll/userregisterform.html',{'form':fm})

def student_info(request): 
    stud = student.objects.all()
    return render(request, 'enroll/student_details.html', {'stu': stud})