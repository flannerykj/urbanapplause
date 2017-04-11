from django.conf.urls import include, url
from . import views
from django.views.generic.base import TemplateView

app_name = 'userprofile'
urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='profile.html'), name='main'),
    url(r'^edit/(?P<pk>\d+)/$', views.UpdateProfile.as_view(), name='edit'),
]