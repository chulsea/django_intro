from django.shortcuts import render, render_to_response, HttpResponse
from django.template import RequestContext
from pprint import pprint
import random

# Create your views here.
def index(request):
    return HttpResponse('Welcome to Django!')
    
def dinner(request):
    menus = ['맘스터치', '소고기덮밥', '태평소국밥', '브리또', '차돌박이']
    return render(request, 'home/dinner.html', {
        'menus': menus,
        'pick': random.choice(menus)
    })
    
def hello(request, name):
    return render(request, 'home/hello.html', {'name': name})

def cube(request, num):
    return render(request, 'home/cube.html', {'result': num**3})
    
def ping(request):
    return render(request, 'home/ping.html')
    
def pong(request):
    data = request.GET.get('data')
    return render(request, 'home/pong.html', {
        'data': data
        })
        
def user_new(request):
    return render(request, 'home/new.html')
    
def user_create(request):
    nickname = request.POST.get('nickname')
    pwd = request.POST.get('pwd')
    return render(request, 'home/create.html', {'nickname': nickname, 'pwd': pwd})
    