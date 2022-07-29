from django.shortcuts import render
from django.views.generic import TemplateView, UpdateView
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView
from django.views import View
from .models import Post, Booking




class PostView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class BookingListView(ListView):

    model = Booking
    template_name = 'booking-list.html'
    queryset = Booking.objects.all().order_by('created_on')
    paginate_by = 10


class AddBookingView(CreateView):
    model: Booking
    template_name = 'new-booking.html'

# class PostUpdateView(generic.UpdateView):
#     template_name = 'post-update.html'
#     model = Post

#     fields = [
#         "location",
#         "date",
#         "time",
#         "adult_price",
#         "child_price"
#     ]
#     success_url = "/"
