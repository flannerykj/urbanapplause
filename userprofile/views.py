from django.shortcuts import render
from django.views.generic.edit import UpdateView
from userprofile.models import Profile

# Create your views here.
class UpdateProfile(UpdateView):
    model = Profile
    fields = '__all__'
    template_name = 'edit.html'
    success_url = '/profile'