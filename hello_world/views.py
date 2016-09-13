from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    display = 'Hello World'
    return HttpResponse(display)


def hello_name(request):
    display = 'Hello Alvin this is hello_name function inside hello_world.views'
    return HttpResponse(display)
