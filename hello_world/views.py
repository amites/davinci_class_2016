from django.http import HttpResponse
from django.shortcuts import render

from hello_world.models import Rating, StuffToRate


def index(request):
    display = ''
    objs = StuffToRate.objects.all()
    obj = objs[0]
    display += '{} - {} - {}'.format(obj.title, obj.color, obj.get_rating())
    # return HttpResponse(display)
    context = {
        'objs': objs,
        # 'obj': obj,
    }
    return render(request, 'base.html', context)


def hello_name(request):
    display = 'Hello Alvin this is hello_name function inside hello_world.views'
    return HttpResponse(display)
