from django.shortcuts import render
from django.views.generic import ListView
from .models import Post, Category
from django.shortcuts import render_to_response, get_object_or_404
from django.utils import timezone
from django.views import generic
from django.core.paginator import Paginator

class IndexView(ListView):
    model = Post
    template_name = "blog-index.html"

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['page_title'] = "All posts"
        context['category_list'] = Category.objects.all()
        context['complete_list'] = Post.objects.all().order_by('-pub_date')
        paginator = Paginator(context['complete_list'], 10)
        context['object_list'] = paginator.page(1)
        return context

class CategoryIndexView(ListView):
    model = Post
    template_name = "blog-index.html"
    def get_context_data(self, **kwargs):
        context = super(CategoryIndexView, self).get_context_data(**kwargs)
        category = Category.objects.get(slug=self.kwargs['category'])
        context['page_title'] = category.title+" Posts"
        context['object_list'] = Post.objects.filter(category=category).order_by('-pub_date')
        context['category_list'] = Category.objects.all()
        return context

class TagIndexView(ListView):
	model = Post
 	template_name = "blog-index.html"
 	def get_context_data(self, **kwargs):
 		context = super(TagIndexView, self).get_context_data(**kwargs)
 		context['page_title'] = " Posts tagged "+self.kwargs['tag']
 		context['object_list'] = Post.objects.filter(tags__name__in=[self.kwargs['tag']]).order_by('-pub_date')
 		context['category_list'] = Category.objects.all()
 		return context

class DetailView(generic.DetailView):
    model = Post
    template_name = 'blog-detail.html'