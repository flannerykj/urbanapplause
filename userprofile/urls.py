from django.conf.urls import include, url
from . import views
from django.views.generic.base import TemplateView

app_name = 'userprofile'
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.UserProfile.as_view(), name='main'),
    url(r'^edit/(?P<pk>\d+)/$', views.UpdateProfile.as_view(), name='edit'),
]