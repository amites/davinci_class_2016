from django import forms

from hello_world.models import Pet, Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['stuff', 'rating', ]


class PetSearchForm(forms.ModelForm):
    breed = forms.CharField(required=False)

    class Meta:
        model = Pet
        fields = ['name', 'breed', ]
