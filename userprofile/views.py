from django.shortcuts import render
from django.views.generic.edit import UpdateView
from userprofile.models import Profile
from performances.models import Performance
from .forms import ProfileForm
from django.views import generic

# Create your views here.
class UpdateProfile(UpdateView):
    model = Profile
    template_name = 'edit.html'
    success_url = '/profile'
    form_class = ProfileForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UpdateProfile, self).get_context_data(**kwargs)
        context['page_title'] = "Edit Profile"
        context['cancel_url'] = "/profile"
        return context

class UserProfile(generic.DetailView):
    model = Profile
    template_name = 'profile.html'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UserProfile, self).get_context_data(**kwargs)
        context['applause'] = Performance.objects.filter(audience__id=self.object.id)
        return context