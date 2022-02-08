from ftplib import FTP_TLS
from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from django.contrib.auth import update_session_auth_hash


#Sign_up 
def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
           fm.save()
           messages.success(request,'Account has been create successfully')
        fm = SignUpForm()
    else:
        fm = SignUpForm()
    return render (request, 'enroll/signup.html', {'form':fm})

# Log_in views 
def user_login (request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None :
                    login(request, user)
                    messages.success(request , 'Login successfully....!!!')
                    return HttpResponseRedirect('/profile/')
                else:
                    messages.success(request,'Enter valid username & password')
        else:
            fm = AuthenticationForm()
        return render (request , 'enroll/userlogin.html', {'form':fm})
    else:
        return HttpResponseRedirect('/profile/')
    
#profile 
def profile(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/profile.html')
    else:
        return HttpResponseRedirect('/login/')

#Log Out 
def log_out(request):
    logout(request)
    return  HttpResponseRedirect('/login/')  

#Change Password with Odd pass 

def User_change_pass(request):
    if request.user.is_authenticated:
        if request.method == "POST":
            fm = PasswordChangeForm(user= request.user, data = request.POST)
            if fm.is_valid():
                fm.save()
                update_session_auth_hash(request,fm.user)
                return HttpResponseRedirect('/profile/')
        else:
            fm = PasswordChangeForm(user =request.user)
        return render(request, 'enroll/changepass.html',{'form':fm})
    else:
       return HttpResponseRedirect('/login/') 