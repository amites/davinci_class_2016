from django import forms

from hello_world.models import Customer, Pet, Rating, Order, Service


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['stuff', 'rating', ]


class PetSearchForm(forms.ModelForm):
    breed = forms.CharField(required=False)

    class Meta:
        model = Pet
        fields = ['name', 'breed', ]


class OrderForm(forms.ModelForm):
    service = forms.ModelMultipleChoiceField(
        queryset=Service.objects.all(),
        widget=forms.CheckboxSelectMultiple()
    )

    class Meta:
        model = Order
        fields = ['customer', 'service', 'week_day']


class NewOrderForm(forms.Form):
    customer = forms.ModelChoiceField(Customer.objects.all())
    mileage = forms.IntegerField(max_value=1000, min_value=0)
