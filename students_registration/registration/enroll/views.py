from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def sign_up(request):
    if request.method == "POST":
        fm = UserCreationForm(request.POST)
        if fm.is_valid():
           fm.save()
        fm = UserCreationForm()
    else:
        fm = UserCreationForm()
    return render (request, 'enroll/signup.html', {'form':fm})
