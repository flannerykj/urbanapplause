from django.conf.urls import url

from . import views

app_name = 'artists'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    url(r'^edit/(?P<pk>\d+)/$', views.UpdateArtist.as_view(), name='edit'),
    url(r'^create/$', views.CreateArtist.as_view(), name='create'),
    url(r'^delete/(?P<pk>\d+)$', views.DeleteArtist.as_view(), name='delete')
]