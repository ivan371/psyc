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
     url(r'^self_room/', Self_room.as_view(), name="self_room"),
     url(r'^self_update/', Self_update.as_view(), name="self_update"),
     url(r'^list_article/', List_article.as_view(), name="list_article"),
     url(r'^create_article/', Create_article.as_view(), name="create_article"),
      url(r'^(?P<pk>\d+)/$', Show_user.as_view(), name="detail"),
      url(r'^users/$', Show_users.as_view(), name="users"),
]
