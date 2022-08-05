from django.contrib import admin
from .models import Booking, Meal, Post

admin.site.register(Booking)
admin.site.register(Meal)
admin.site.register(Post)


class ArticleAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("booking_number",)}


