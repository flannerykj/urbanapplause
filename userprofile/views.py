from django.shortcuts import render
from django.views.generic.edit import UpdateView
from userprofile.models import Profile
from performances.models import Performance, Applause
from .forms import ProfileForm
from django.views import generic
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User

# Create your views here.
class UpdateProfile(UpdateView):
    model = Profile
    template_name = 'form.html'
    form_class = ProfileForm
    def form_valid(self, form):
        obj = form.save()
        return HttpResponseRedirect('/profile/'+str(self.object.id))
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
        context['performances0'] = Performance.objects.filter(audience__id=self.object.id)
        performances = []; 
        for p in context['performances0']: 
            p.datetime = Applause.objects.filter(performance=p, user=self.request.user)[0].datetime
            performances.append(p)
        context['performances'] = sorted(performances, key=lambda performance: performance.datetime, reverse=True)
        return context

class CreateMusician(UpdateView):
    model = User
    template_name = 'form.html'
    fields = ['musician',]
    def form_valid(self, form):
        obj = form.save()
        return HttpResponseRedirect('/profile/'+str(self.request.user.id))
    def get_object(self, queryset=None):
        '''This method will load the object
           that will be used to load the form
           that will be edited'''
        return self.request.user