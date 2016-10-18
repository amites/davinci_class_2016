from django.http import HttpResponse
from django.shortcuts import render

from hello_world.forms import NewOrderForm, PetSearchForm, RatingForm, OrderForm
from hello_world.models import Customer, Pet, Rating, StuffToRate


def index(request):
    # if request.method == 'POST':
    #     form = RatingForm(request.POST)
    #     if form.is_valid():
    #         form.save()
    # else:
    #     form = RatingForm()

    # import ipdb
    # ipdb.set_trace()

    if request.method == 'POST':

        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = OrderForm()

    pets = []
    # if request.method == 'POST':
    #     form = PetSearchForm(request.POST)
    #     if form.is_valid():
    #         # cleaned_data is a dict populated by running is_valid
    #         # the dict values available are only those set from the
    #         # fields property
    #         search_dict = {}
    #         for field_name, field_value in form.cleaned_data.iteritems():
    #             if field_value:
    #                 search_dict[field_name] = field_value
    #         # pet_name = form.cleaned_data['name']
    #         # pets = Pet.objects.filter(name=pet_name)
    #         print 'Search dict:\n\t{}'.format(str(search_dict))
    #         pets = Pet.objects.filter(**search_dict)
    # else:
    #     form = PetSearchForm()
    objs = StuffToRate.objects.all()
    thing = StuffToRate.objects.get(id=1)
    context = {
        'objs': objs,
        'giraffe': thing,
        'form': form,
        'pets': pets,
    }
    return render(request, 'base.html', context)


def hello_name(request):
    # display = 'Hello Alvin this is hello_name function inside hello_world.views'
    # return HttpResponse(display)

    if request.method == 'POST':

        customer_id = request.POST['customer']
        cust = Customer.objects.get(id=customer_id)
        data = {
            'customer': cust,
            'mileage': cust.mileage * 2,
        }
        # print '------------------ \n {} \n --------------------'.format(data)
        form = NewOrderForm(initial=data)
        if form.is_valid():
            pass
    else:
        form = NewOrderForm()

    context = {
        'form': form,
    }

    return render(request, 'base.html', context)
