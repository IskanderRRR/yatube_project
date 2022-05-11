from django.shortcuts import render
from django.http import HttpResponse
from django.http import HttpRequest


def index(request):    
    return HttpResponse('Главная страница')


def group_posts(request,slug):
    return HttpResponse('Публикации')

# Create your views here.
