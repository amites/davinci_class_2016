from django import forms

from hello_world.models import Rating


class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['stuff', 'rating', ]
