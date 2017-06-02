from django.conf.urls import url

from . import views

app_name = 'talent'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^musicians/$', views.MusicianIndex.as_view(), name='musicians'),
    url(r'^musicians/(?P<pk>[0-9]+)/$', views.MusicianDetail.as_view(), name='musician-detail'),
    url(r'^musicians/(?P<pk>\d+)/edit/$', views.UpdateMusician.as_view(), name='musician-edit'),
    url(r'^musicians/create/$', views.MusicianCreate.as_view(), name='musician-create'),
    url(r'^musicians/(?P<pk>\d+)/delete/$', views.DeleteTalent.as_view(), name='musician-delete'),
    url(r'^artists/$', views.ArtistIndex.as_view(), name='artists'),
    url(r'^artists/(?P<pk>[0-9]+)/$', views.ArtistDetail.as_view(), name='artist-detail'),
    url(r'^artists/(?P<pk>\d+)/edit/$', views.UpdateArtist.as_view(), name='artist-edit'),
    url(r'^artists/create/$', views.ArtistCreate.as_view(), name='artist-create'),
]