from . import views
from django.urls import path
from .views import AddBookingView, BookingListView, PostUpdateView


urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    path('new-booking/', AddBookingView.as_view(), name='new-booking'),
    path('booking-list/', BookingListView.as_view(), name='booking-list'),
    path('<slug:slug>/edit', PostUpdateView.as_view(), name='post-update')
]