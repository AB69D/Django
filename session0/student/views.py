from importlib.resources import path
from django.shortcuts import render


def setsession(request):
    request.session['name'] = 'Abid'
    request.session['email'] = 'khanabid7474@gmail.com'
    return render(request, 'student/set_sessions.html')


def getsession(request):
    #user = request.session['name']
    user =  request.session.get('name',default='Guest')
    email = request.session.get('email',
                                default = 'guest@gmail.com')
    keys = request.session.keys()
    items = request.session.items()
    age = request.session.setdefault('age','21')
    return render(request, 'student/get_sessions.html',
                  {'user': user, 'email': email,'age':age, 'keys': keys, 'items':items},)

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
        del request.session['email']
    return render(request, 'student/del_sessions.html')

def flush(request):
    request.session.flush()
    return render(request, 'student/del_sessions.html')
