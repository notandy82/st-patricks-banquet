from django.shortcuts import render
from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views import View
from .models import Post, Booking
from .forms import NewBooking, EditPost
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin





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

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            reference_name=self.request.user
        )

 

class AddBookingView(LoginRequiredMixin, CreateView):
    model: Booking
    form_class = NewBooking
    template_name = 'new-booking.html'
    success_url = '/booking-list/'
    

    def dispatch(self, request, *args, **kwargs):
        self.request = request
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.reference_name = self.request.user
        obj.save()
        return super().form_valid(form)
        


class PostEditView(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = EditPost
    template_name = 'post-update.html'
    success_url = '/'


class BookingEditView(LoginRequiredMixin, UpdateView):
    model = Booking
    form_class = NewBooking
    template_name = 'booking-edit.html'
    success_url = '/booking-list/'
    

class DeleteBookingView(LoginRequiredMixin, DeleteView):
    model = Booking
    template_name = 'delete-booking.html'
    success_url = '/booking-list/'


class BookingDetailView(DetailView):
    model = Booking
    template_name = 'booking_detail.html'