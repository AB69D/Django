from django.shortcuts import render

from .models import student

from .forms import studentregistration

def showformdata(request):
    if request.method == 'POST':
        fm = studentregistration(request.POST)
        if fm.is_valid():
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']
            pm = fm.cleaned_data['password']
            rw = student(name = nm, email = em, password = pm)
            rw.save()
            fm= studentregistration()
    else:
        fm = studentregistration()
    return render(request, 'student/userregistration.html',{'form':fm})
