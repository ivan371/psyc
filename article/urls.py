from django.conf.urls import url
from .views import *
from django.contrib import admin

urlpatterns = [
    url(r'^last_article/', Last_article.as_view(), name="last_article"),
]
