from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Artist
from django.core.urlresolvers import reverse_lazy
from .forms import ArtistForm
from django.views.generic import ListView


class IndexView(ListView):
    model = Artist
    template_name = "artist-index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['object_list'] = Artist.objects.all()
        context['page_title'] = "Artists"
        context['model_type'] = "Artist"
        return context

class DetailView(generic.DetailView):
    model = Artist
    template_name = 'detail.html'

class UpdateArtist(UpdateView):
    model = Artist
    template_name = 'edit.html'
    form_class = ArtistForm
    def get_success_url(self):
        return reverse_lazy('artists:detail', kwargs={'pk': self.object.id})
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(UpdateArtist, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_title'] = "Edit Artist"
        context['model_type'] = "Artist"
        context['cancel_url'] = reverse_lazy('artists:detail', kwargs={'pk': self.object.id})
        context['submit_text'] = "Save"
        return context


class CreateArtist(CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'edit.html'
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()        
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return '/artists/'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CreateArtist, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_title'] = "Add Artist"
        context['model_type'] = "Artist"
        context['cancel_url'] = "/artists"
        context['submit_text'] = "Save"
        return context

class DeleteArtist(DeleteView):
    model = Artist
    success_url = '/artists/'
    template_name = 'edit.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DeleteArtist, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_title'] = "Delete Artist?"
        context['model_type'] = "Artist"
        context['cancel_url'] = "/artists"
        context['submit_text'] = "Delete"
        return context