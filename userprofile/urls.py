from django.conf import settings
from django.conf.urls.static import static

from django.conf.urls import include, url
from . import views
from django.views.generic.base import TemplateView

app_name = 'userprofile'
urlpatterns = [
    url(r'^(?P<pk>\d+)/$', views.UserProfile.as_view(), name='main'),
    url(r'^(?P<pk>\d+)/edit$', views.UpdateProfile.as_view(), name='edit'),
    url(r'^(?P<pk>\d+)/create-musician-profile$', views.CreateMusician.as_view(), name='create-musician'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)