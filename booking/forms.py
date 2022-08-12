from django import forms
from .models import Booking, Post


class NewBooking(forms.ModelForm):
    """ Form to register number of attendees """

    class Meta:
        model = Booking
        fields = (
            'adult_meat',
            'adult_vegetarian',
            'children',
            'highchairs',
            'additional_info',
            )
        widgets = {
            'additional_info': forms.Textarea(
                attrs={'placeholder': 'Please include any\
                    dietary restrictions'}),
        }


class EditPost(forms.ModelForm):
    """ Form to edit event details """

    class Meta:
        model = Post
        fields = (
            'event',
            'location',
            'date',
            'time',
            'adult_price',
            'child_price'
        )
