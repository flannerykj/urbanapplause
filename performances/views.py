from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.views import generic
from django.views.generic.edit import UpdateView, CreateView, DeleteView
from django.views.generic import ListView
from .models import Performance, Participation, Applause
from .forms import PerformanceForm
import sys
from datetime import datetime, timedelta, tzinfo
from django.core.paginator import Paginator

from django.http import HttpResponse
try:
    from django.utils import simplejson as json
except ImportError:
    import json
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
# Create your views here.

class IndexView(ListView):
    model = Performance
    template_name = "performance-index.html"
    paginate_by = 10
    context_object_name = 'object_list'
    queryset = Performance.objects.filter(end_time__gt=datetime.now()).order_by('-start_time')
    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['object_list'] = Performance.objects.filter(end_time__gt=datetime.now()).order_by('-start_time')
        for p in context['object_list']:
        	if Applause.objects.filter(performance=p, user=self.request.user):
        		p.notapplauded = ''
        	else:
        		p.applauded = 'btn-info'
        return context

class IndexViewArchive(ListView):
    model = Performance
    template_name = "performance-index.html"
    paginate_by = 5
    def get_context_data(self, **kwargs):
        context = super(IndexViewArchive, self).get_context_data(**kwargs)
        context['object_list'] = Performance.objects.filter(end_time__lt=datetime.now()).order_by('start_time')
        context['archive'] = 'true'
        for p in context['object_list']:
            p.ended = p.end_time
            if Applause.objects.filter(performance=p, user=self.request.user):
                p.notapplauded = ''
            else:
                p.applauded = 'btn-info'
        return context

@login_required
@require_POST
def applaud(request):
	if request.method == 'POST':
		user = request.user
		post_id = request.POST.get('id', None)
		performance = get_object_or_404(Performance, id=post_id)
		user_applause = Applause.objects.filter(performance=performance, user=user)
		if user_applause:
			user_applause.delete()
			message = 'Removed from audience'
			added = 'false'
		else:
			a = Applause.objects.create(user=user, performance=performance)
			message = str(a.user.username)
			added = 'true'

	ctx = {'audience_count': performance.total_audience, 'message': message, 'post_id': post_id, 'added': added}
	# use mimetype instead of content_type if django < 5
	return HttpResponse(json.dumps(ctx), content_type='application/json')

class AddPerformance(CreateView):
    model = Performance
    form_class = PerformanceForm
    template_name = 'form.html'
    def form_valid(self, form):
        obj = form.save(commit=False) 
        for musician in form.cleaned_data['musicians']:
            participation = Participation()
            obj.save()
            participation.performance = obj
            participation.musician = musician
            participation.performance.save()
            participation.musician.save()
            participation.save()
        obj.save()
        return HttpResponseRedirect(self.get_success_url())
    def get_success_url(self):
        return '/performances/'
    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(AddPerformance, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['page_title'] = "Add Performance"
        context['model_type'] = "Performance"
        context['cancel_url'] = "/performances"
        context['submit_text'] = "Save"
        return context


