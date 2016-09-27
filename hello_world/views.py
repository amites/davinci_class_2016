from django.http import HttpResponse
from django.shortcuts import render

from hello_world.models import Rating, StuffToRate


def index(request):
    objs = StuffToRate.objects.all()
    thing = StuffToRate.objects.get(id=1)
    context = {
        'objs': objs,
        'giraffe': thing,
    }
    return render(request, 'base.html', context)


def hello_name(request):
    display = 'Hello Alvin this is hello_name function inside hello_world.views'
    return HttpResponse(display)
