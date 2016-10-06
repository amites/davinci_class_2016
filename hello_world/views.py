from django.http import HttpResponse
from django.shortcuts import render

from hello_world.forms import RatingForm
from hello_world.models import Rating, StuffToRate


def index(request):
    if request.method == 'POST':
        data = dict(request.POST)
        multi_value = data.pop('multi_rating')
        print '---------\n {}\n ----------'.format(str(data))

        form = RatingForm(data)

        if form.is_valid():
            form.save()
    else:
        form = RatingForm()
    objs = StuffToRate.objects.all()
    thing = StuffToRate.objects.get(id=1)
    context = {
        'objs': objs,
        'giraffe': thing,
        'form': form,
    }
    return render(request, 'base.html', context)


def hello_name(request):
    display = 'Hello Alvin this is hello_name function inside hello_world.views'
    return HttpResponse(display)
