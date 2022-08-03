from django import forms
from .models import Booking, Post

class NewBooking(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('reference_name', 'adults', 'children', 'highchairs', 'additional_info')


class NewPost(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('event', 'location', 'date', 'time', 'adult_price', 'child_price')