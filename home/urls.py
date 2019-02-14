from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.user_create, name='create'),
    path('new/', views.user_new, name='new'),
    path('pong/', views.pong, name='pong'),
    path('ping/', views.ping, name='ping'),
    path('cube/<int:num>/', views.cube, name='cube'),
    path('hello/<name>/', views.hello, name='hello'),
    path('dinner/', views.dinner, name='dinner'),
    path('index/', views.index, name='index'),
]
