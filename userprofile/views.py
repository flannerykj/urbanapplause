from django.shortcuts import render
from django.views.generic.edit import UpdateView
from userprofile.models import Profile
from .forms import ProfileForm

# Create your views here.
class UpdateProfile(UpdateView):
    model = Profile
    template_name = 'edit.html'
    success_url = '/profile'
    form_class = ProfileForm

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UpdateProfile, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_title'] = "Edit Profile"
        context['cancel_url'] = "/profile"
        return context