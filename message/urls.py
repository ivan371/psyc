from django.conf.urls import url
from .views import *
from django.contrib import admin

urlpatterns = [
      url(r'^(?P<pk>\d+)/$', Showchat.as_view(), name="detail"),
      url(r'^(?P<pk>\d+)/create/$', create_message, name="create"),
]
