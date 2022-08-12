from django.db import models
from django.contrib.auth.models import User


PAID_CHOICES = (('NP', 'Not Paid'), ('PA', 'Payment Accepted'))


class Common(models.Model):
    """ Model to allow pricing to be used in multiple models """
    adult_price = models.SmallIntegerField(
        default=150,
        null=False,
        blank=False
    )
    child_price = models.SmallIntegerField(
        default=100,
        null=False,
        blank=False
    )

    class Meta:
        """ Prevent creation of separate model """
        abstract = True


class Booking(Common):
    """ Model for selecting number of attendees for each booking """
    booking_number = models.BigAutoField(primary_key=True)
    reference_name = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        blank=True
    )
    adult_meat = models.SmallIntegerField(null=True, blank=True)
    adult_vegetarian = models.SmallIntegerField(null=True, blank=True)
    children = models.SmallIntegerField(null=True, blank=True)
    highchairs = models.SmallIntegerField(null=True, blank=True)
    payment = models.CharField(
        choices=PAID_CHOICES,
        default='NP',
        max_length=12
    )
    additional_info = models.TextField(null=True, blank=True, max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        """ Determine ordering in admin panel """
        ordering = ['created_on']

    def __int__(self):
        return self.booking_number


class Post(Common):
    """ Model for event information """
    id = models.BigAutoField(primary_key=True)
    event = models.CharField(max_length=40, null=False, blank=False)
    location = models.CharField(max_length=40)
    date = models.DateField(null=False, blank=False)
    time = models.TimeField(null=False, blank=False)
    slug = models.SlugField(null=False)

    def __str__(self):
        return self.event
