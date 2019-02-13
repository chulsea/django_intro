from django.shortcuts import render, HttpResponse
from pprint import pprint
import random

# Create your views here.
def index(request):
    return HttpResponse('Welcome to Django!')
    
def dinner(request):
    menus = ['맘스터치', '소고기덮밥', '태평소국밥', '브리또', '차돌박이']
    return render(request, 'dinner.html', {
        'menus': menus,
        'pick': random.choice(menus)
    })