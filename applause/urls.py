from django.conf.urls import url

from . import views

app_name = 'applause'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^add/(?P<talent_type>[a-z]+)$', views.AddApplause.as_view(), name='add'),
]