from django import forms

from hello_world.models import Rating, RATING_VALUES


class RatingForm(forms.ModelForm):
    multi_rating = forms.MultipleChoiceField(required=False, choices=RATING_VALUES,
                                       widget=forms.CheckboxSelectMultiple)

    class Meta:
        model = Rating
        fields = ['stuff', 'multi_rating', ]
