from importlib.resources import path
from django.shortcuts import render
from datetime import datetime , timedelta

def setcookies(request):
    response = render(request,'student/set_cookies.html')
    response.set_signed_cookie('name','abid',salt='nm',expires=datetime.utcnow()+timedelta(days=2)
                        ) # age should be in second 
    return response 

def getcookies(request):
    #name = request.COOKIES['name']
    #name =  request.COOKIES.get('name',"Guest")
    name =  request.get_signed_cookie('name', salt='nm')
    return render(request, 'student/get_cookies.html',
                  {'user': name})


def delcookies(request):
    de = render(request,'student/del_cookies.html')
    de.delete_cookie('name')
    return de