from django.http.request import HttpRequest
from django.shortcuts import render
from .models import url 
import uuid
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request, 'shortner/index.html')
def create(request):
    if request.method == 'post':
        url =  request.post['link']
        uid = str(uuid.uuid4())[:5]
        new_url =  url(link = link  , uuid =  uid)
        new_url.save()
        return HttpResponse(uid)