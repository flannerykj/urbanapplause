from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth import views as auth_views
from . import views
from django.views.generic.base import TemplateView

urlpatterns = [
    url(r'^$', TemplateView.as_view(template_name='home.html'), name='home'),
    url(r'^login/$', auth_views.login, {'template_name': 'login.html'}, name='login'),
    url(r'^logout/$', auth_views.logout, {'template_name': 'logged_out.html'}, name='logout'),
    url(r'^signup/$', views.signup, name='signup'),
    url(r'^profile/', include('userprofile.urls')),
    url(r'^performances/', include('performances.urls')),
    url(r'^musicians/', include('musicians.urls')),
    url(r'^admin/', admin.site.urls),
]
