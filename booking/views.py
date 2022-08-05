from django.shortcuts import render
from django.views.generic import TemplateView
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views import View
from .models import Post, Booking
from .forms import NewBooking, EditPost
from django.contrib.auth.mixins import LoginRequiredMixin




class PostView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class BookingListView(LoginRequiredMixin, ListView):

    model = Booking
    template_name = 'booking-list.html'
    queryset = Booking.objects.all().order_by('created_on')
    paginate_by = 10


class AddBookingView(LoginRequiredMixin, CreateView):
    model: Booking
    form_class = NewBooking
    template_name = 'new-booking.html'
    success_url = '/booking-list/'


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = EditPost
    template_name = 'post-update.html'
    success_url = '/'


class BookingEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = NewBooking
    template_name = 'booking-edit.html'
    success_url = '/booking-list/'
