from django import forms
from .models import Booking, Post

class NewBooking(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('adult_meat', 'adult_vegetarian', 'children', 'highchairs',
         'additional_info')


class EditPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('event', 'location', 'date', 'time', 'adult_price',
         'child_price')