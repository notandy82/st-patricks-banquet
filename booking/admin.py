from django.contrib import admin
from .models import Booking, Post

admin.site.register(Booking)
admin.site.register(Post)


class BookingAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("booking_number",)}


