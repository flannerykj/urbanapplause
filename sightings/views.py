from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Sighting
from django.core.urlresolvers import reverse_lazy
from .forms import SightingForm
from django.views.generic import ListView
# Create your views here.

class IndexView(ListView):
    model = Sighting
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['sighting_list'] = Sighting.objects.all().order_by('-datetime')
        context['page_title'] = "Sightings"
        context['model_type'] = "Sighting"
        return context

class DetailView(generic.DetailView):
    model = Sighting
    template_name = 'detail.html'


class AddSighting(CreateView):
    model = Sighting
    form_class = SightingForm
    template_name = 'edit.html'
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()        
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return '/sightings'