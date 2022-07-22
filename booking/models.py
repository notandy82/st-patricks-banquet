from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

PAID_CHOICES = ((0, 'Not Paid'), (1, 'Payment Accepted'))
MEAL_CHOICES = (('M', 'Meat'), ('V', 'Vegetarian'), ('C', 'Child'))

class Book(models.Model):
    booking_number = models.BigAutoField(primary_key=True,)
    reference_name = models.ForeignKey(User, on_delete=models.CASCADE)
    adults = models.SmallIntegerField(null=False, blank=False)
    children = models.SmallIntegerField(null=True, blank=True)
    highchairs = models.SmallIntegerField(null=True, blank=True)
    payment = models.IntegerField(choices=PAID_CHOICES, default=0)
    additional_info = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_on']
    
    def __str__(self):
        return self.booking_number

class Meals(models.Model):
    number = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=30, null=False, blank=False)
    food = models.CharField(max_length=1, choices=MEAL_CHOICES, null=False, blank=False)
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



