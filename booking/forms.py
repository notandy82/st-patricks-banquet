from django import forms
from .models import Booking

class NewBooking(forms.ModelForm):

    class Meta:
        model = Booking
        fields = ('reference_name', 'adults', 'children', 'highchairs', 'additional_info')

        