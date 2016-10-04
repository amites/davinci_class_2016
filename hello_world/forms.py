from django import forms

from hello_world.models import Customer, Pet, Rating, Order


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
    class Meta:
        model = Order
        fields = ['customer', 'service', ]


class NewOrderForm(forms.Form):
    customer = forms.ModelChoiceField(Customer.objects.all())
    mileage = forms.IntegerField(max_value=1000, min_value=0)
