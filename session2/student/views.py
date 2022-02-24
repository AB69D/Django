from importlib.resources import path
from django.shortcuts import render

def settestcookie(request):
    request.session.set_test_cookie()
    return render(request, 'student/set_sessions.html')


def checktestcookie(request):
    request.session.test_cookie_worked()
    print(request.session.test_cookie_worked())
    return render(request, 'student/check_sessions.html')


def deltestcookie(request):
    request.session.delete_test_cookie()
    return render(request, 'student/del_test_sessions.html')



