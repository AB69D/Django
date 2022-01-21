from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def fees_django(request):
    name = 'md. manzurul islam'
    fee = '300'
    context_dic = {'nm': name,'fees': fee} 
    return render(request, 'fees1.html', context_dic )
        

def fees_python(request):
    student ={'names' : ['abid','omi']}
    return render(request, 'fees2.html', student )
    