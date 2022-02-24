from importlib.resources import path
from django.shortcuts import render


def setsession(request):
    request.session['name'] = 'Abid'
    request.session['email'] = 'khanabid7474@gmail.com'
    request.session.set_expiry(300)
    #request.session.set_expiry(0)  for set the age after closing the browser
    
    
    return render(request, 'student/set_sessions.html')


def getsession(request):
    #user = request.session['name']
    user =  request.session['name']
    email = request.session['email']
    
    print(request.session.get_session_cookie_age,
    request.session.get_expiry_age,
    request.session.get_expiry_date,
    request.session.get_expire_at_browser_close)
    
    return render(request, 'student/get_sessions.html',
                  {'user': user, 'email': email})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
        del request.session['email']
    return render(request, 'student/del_sessions.html')

def flush(request):
    request.session.flush()
    # for clear in databage
    request.session.clear_expired()
    return render(request, 'student/del_sessions.html')
