from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from .models import Applause
from talent.models import Talent
from django.core.urlresolvers import reverse_lazy
from .forms import ApplauseForm
from django.views.generic import ListView
from django.db.models import Count
# Create your views here.

class IndexView(ListView):
    model = Applause
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(IndexView, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['object_list'] = Applause.objects.all().order_by('-pub_date')
        context['object_list1'] = Talent.objects.annotate(num_applause=Count('applause')).order_by('-num_applause')[:5]
        context['page_title'] = "Applause"
        context['model_type'] = "Applause"
        context['base_url'] = "/applause"
        return context

class DetailView(generic.DetailView):
    model = Applause
    template_name = 'detail.html'

class AddApplause(CreateView):
    model = Applause
    form_class = ApplauseForm
    template_name = 'edit.html'
    def get_form_kwargs(self):
        kwargs = super( AddApplause, self).get_form_kwargs()
        # update the kwargs for the form init method with yours
        kwargs.update(self.kwargs)  # self.kwargs contains all url conf params
        return kwargs
    def get_success_url(self):
        return '/applause/'
    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        obj.save()        
        return HttpResponseRedirect(self.get_success_url())
    def get_context_data(self, **kwargs):
    	talent_type = self.kwargs['talent_type']
        # Call the base implementation first to get a context
        context = super(AddApplause, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_title'] = "Add "+talent_type
        context['model_type'] = "Applause"
        context['cancel_url'] = "/applause"
        context['submit_text'] = "Save"
        return context




