from . import views
from django.urls import path
from .views import (
    AddBookingView,
    BookingListView,
    PostEditView,
    BookingEditView,
    DeleteBookingView,
    )

urlpatterns = [
    path('', views.PostView.as_view(), name='home'),
    path('new-booking/', AddBookingView.as_view(), name='new-booking'),
    path('booking-list/', BookingListView.as_view(), name='booking-list'),
    path('<slug:slug>/edit/', PostEditView.as_view(), name='post-update'),
    path('edit-booking/<int:pk>/', BookingEditView.as_view(),
        name='booking-edit'),
    path('delete-booking/<int:pk>/', DeleteBookingView.as_view(),
        name='booking-delete'),
]
