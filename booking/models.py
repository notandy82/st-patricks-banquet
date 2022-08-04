from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField
import datetime

PAID_CHOICES = (('NP', 'Not Paid'), ('PA', 'Payment Accepted'))
MEAL_CHOICES = (('M', 'Meat'), ('V', 'Vegetarian'), ('C', 'Child'))

class DbLimitException(BaseException):
    pass


class Booking(models.Model):
    """Model for selecting number of attendees for each booking"""
    booking_number = models.BigAutoField(primary_key=True)
    reference_name = models.ForeignKey(User, on_delete=models.CASCADE)
    adults = models.SmallIntegerField(null=False, blank=False)
    children = models.SmallIntegerField(null=True, blank=True)
    highchairs = models.SmallIntegerField(null=True, blank=True)
    payment = models.CharField(choices=PAID_CHOICES, default='Not Paid', max_length=12)
    additional_info = models.TextField(null=True, blank=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __int__(self):
        return self.booking_number


class Meal(models.Model):
    """Model for meal choice for individual attendees"""
    number = models.ForeignKey(Booking, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=False, blank=False)
    food = models.CharField(max_length=1, choices=MEAL_CHOICES, null=False,
                blank=False)
    dairy = models.BooleanField(default=False)
    gluten = models.BooleanField(default=False)
    nuts = models.BooleanField(default=False)
    peanuts = models.BooleanField(default=False)
    egg = models.BooleanField(default=False)
    shellfish = models.BooleanField(default=False)
    soy = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return self.name

class Post(models.Model):
    """Model for event information"""
    id = models.BigAutoField(primary_key=True)
    event = models.CharField(max_length=40, null=False, blank=False)
    location = models.CharField(max_length=40)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    adult_price = models.SmallIntegerField(default=150, null=False, blank=False)
    child_price = models.SmallIntegerField(default=100, null=False, blank=False)
    slug = models.SlugField(null=False)
    

    def __str__(self):
        return self.event