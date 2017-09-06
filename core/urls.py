from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.contrib.auth import views as auth_views
from core.forms import LoginForm

urlpatterns = [
    url(r'^$', views.home, name="home"),
    url(r'^login/$', auth_views.login, {'template_name': 'login-page.html'}, name='login'),
    # url(r'^cadastro/$', views.cadastro, name="cadastro"),
    url(r'^getUserData/(?P<usuario>[0-9]+)/$', views.get_data, name="get_data"),
]
