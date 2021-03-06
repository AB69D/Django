from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import studentregistration
 
def thankyou(request): 
    return render(request, 'student/success.html')

def showformdata(request):
    if request.method == 'POST':
        fm = studentregistration(request.POST)
        print("POST method")
        if fm.is_valid():
            print("Name --> ", fm.cleaned_data['name'])
            print("Email --> ", fm.cleaned_data['email'])
            ##return render(request, 'student/success.html',{'nm': fm.cleaned_data['name']})
            return HttpResponseRedirect('/student/success')    
    else:
        fm = studentregistration()
        print("Get method")
    
    return render(request, 'student/userregistration.html',{'form':fm})