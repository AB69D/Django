from django.shortcuts import render
from .forms import SignUpForm

def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
           fm.save()
        fm = SignUpForm()
    else:
        fm = SignUpForm()
    return render (request, 'enroll/signup.html', {'form':fm})
