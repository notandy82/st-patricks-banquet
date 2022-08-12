from django.views.generic import TemplateView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .models import Post, Booking
from .forms import NewBooking, EditPost


class PostView(TemplateView):
    """ View to display event information on front page """
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(PostView, self).get_context_data(**kwargs)
        context['posts'] = Post.objects.all()
        return context


class BookingListView(LoginRequiredMixin, ListView):
    """ View to list all bookings made by a user """
    model = Booking
    template_name = 'booking-list.html'
    queryset = Booking.objects.all().order_by('created_on')
    paginate_by = 10

    def get_queryset(self, *args, **kwargs):
        return super().get_queryset(*args, **kwargs).filter(
            reference_name=self.request.user
        )


class AddBookingView(LoginRequiredMixin, CreateView):
    """ View to allow user to create a new booking """
    model = Booking
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


class PostEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ View to allow Admin to update the event information """
    model = Post
    form_class = EditPost
    template_name = 'post-update.html'
    success_url = '/'

    def test_func(self):
        return self.request.user.is_superuser


class BookingEditView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    """ View to allow user to update their booking """
    model = Booking
    form_class = NewBooking
    template_name = 'booking-edit.html'
    success_url = '/booking-list/'

    def test_func(self):
        return self.get_object().reference_name == self.request.user


class DeleteBookingView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    """ View to allow user to delete their booking """
    model = Booking
    template_name = 'delete-booking.html'
    success_url = '/booking-list/'

    def test_func(self):
        return self.get_object().reference_name == self.request.user


class BookingDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    """ View to allow user to see individual booking information """
    model = Booking
    template_name = 'booking_detail.html'

    def test_func(self):
        return self.get_object().reference_name == self.request.user
