from django.conf.urls import url

from . import views

app_name = 'performances'
urlpatterns = [
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^archive/$', views.IndexViewArchive.as_view(), name='archive'),
    url(r'^applaud/$', views.applaud, name='applaud'),
    url(r'^add$', views.AddPerformance.as_view(), name='add'),
]