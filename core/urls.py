from django.conf.urls import url
from .views import *
from django.contrib import admin
from django.contrib.auth.views import login, logout

urlpatterns = [
     url(r'^$', home, name='home'),
     url(r'^home/', home, name='home'),
     url(r'^login/', login, {'template_name': 'core/login.html'}, name="login"),
     url(r'^logout/', logout, {'next_page': '../home'}, name="logout"),
     url(r'^registration/', Registration.as_view(), name="registration"),
]
