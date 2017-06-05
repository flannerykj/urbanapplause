from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView
from .models import Musician
from .forms import MusicianForm
# Create your views here.

class IndexView(ListView):
    model = Musician
    template_name = "musician-index.html"

class DetailView(generic.DetailView):
    model = Musician
    template_name = 'musician-detail.html'
    def get_context_data(self, **kwargs):
        context = super(DetailView, self).get_context_data(**kwargs)
        context['talent'] = self.object
        return context

class AddView(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'form.html'
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.save()        
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return '/musicians/'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AddView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_title'] = "Add Musician"
        context['model_type'] = "Musician"
        context['cancel_url'] = "/musicians"
        context['submit_text'] = "Save"
        return context
