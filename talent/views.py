from django.shortcuts import render
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Talent
from .models import Musician
from .models import Artist
from django.core.urlresolvers import reverse_lazy
from .forms import MusicianForm
from .forms import *
from django.views.generic import ListView

#---------------INDEX----------------
#------------------------------------
class IndexView(ListView):
    model = Musician
    template_name = "talent-index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['object_list'] = Musician.objects.all()
        context['page_title'] = "Talent"
        context['talent_type'] = "Talent"
        return context

class MusicianIndex(ListView):
    model = Musician
    template_name = "talent-index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MusicianIndex, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['object_list'] = Musician.objects.all()
        context['page_title'] = "Musicians"
        context['talent_type'] = "Musician"
        context['detail_url'] = ""
        return context

class ArtistIndex(ListView):
    model = Artist
    template_name = "talent-index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ArtistIndex, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['object_list'] = Artist.objects.all()
        context['page_title'] = "Artists"
        context['talent_type'] = "Artist"
        context['detail_url'] = ""
        return context

#---------------DETAIL---------------
#------------------------------------
class MusicianDetail(generic.DetailView):
    model = Musician
    template_name = 'talent-detail.html'
    def get_context_data(self, **kwargs):
        context = super(MusicianDetail, self).get_context_data(**kwargs)
        context['talent'] = self.object
        return context

class ArtistDetail(generic.DetailView):
    model = Artist
    template_name = 'talent-detail.html'
    def get_context_data(self, **kwargs):
        context = super(ArtistDetail, self).get_context_data(**kwargs)
        context['talent'] = self.object
        return context

#---------------UPDATE---------------
#------------------------------------

class UpdateArtist(UpdateView):
    model = Artist
    template_name = 'edit.html'
    form_class = ArtistForm
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        form.save_m2m()       
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return reverse_lazy('talent:artist-detail', kwargs={'pk': self.object.id})
    def get_context_data(self, **kwargs):
        context = super(UpdateArtist, self).get_context_data(**kwargs)
        context['page_title'] = "Edit Artist"
        context['model_type'] = "Artist"
        context['cancel_url'] = reverse_lazy('talent:artist-detail', kwargs={'pk': self.object.id})
        context['submit_text'] = "Save"
        return context

class UpdateMusician(UpdateView):
    model = Musician
    template_name = 'edit.html'
    form_class = MusicianForm
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        form.save_m2m()       
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return reverse_lazy('talent:musician-detail', kwargs={'pk': self.object.id})
    def get_context_data(self, **kwargs):
        context = super(UpdateMusician, self).get_context_data(**kwargs)
        context['page_title'] = "Edit Musician"
        context['model_type'] = "Musician"
        context['cancel_url'] = reverse_lazy('talent:musician-detail', kwargs={'pk': self.object.id})
        context['submit_text'] = "Save"
        return context

#---------------CREATE---------------
#------------------------------------

class ArtistCreate(CreateView):
    model = Artist
    form_class = ArtistForm
    template_name = 'edit.html'
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        form.save_m2m()       
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return '/talent/artists/'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ArtistCreate, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_title'] = "Add Artist"
        context['model_type'] = "Artist"
        context['cancel_url'] = "/talent/artists/"
        context['submit_text'] = "Save"
        return context

class MusicianCreate(CreateView):
    model = Musician
    form_class = MusicianForm
    template_name = 'edit.html'
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.author = self.request.user
        obj.save()
        form.save_m2m()       
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return '/talent/musicians/'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(MusicianCreate, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_title'] = "Add Musician"
        context['model_type'] = "Muscian"
        context['cancel_url'] = "/talent/musicians/"
        context['submit_text'] = "Save"
        return context

#---------------DELETE---------------
#------------------------------------

class DeleteTalent(DeleteView):
    model = Talent
    success_url = '/talents/'
    template_name = 'edit.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(DeleteTalent, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_title'] = "Delete Talent?"
        context['model_type'] = "Talent"
        context['cancel_url'] = "/talent/"
        context['submit_text'] = "Delete"
        return context