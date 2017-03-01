from __future__ import unicode_literals

from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    rating = models.IntegerField(default=0)
    city = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='avatars', blank=True, null=True)
    number = models.IntegerField(default=0)

class Psycologist(models.Model):

    user = models.ForeignKey(User, related_name="Psycologist")
    rating = models.IntegerField(default=0)

class Client(models.Model):
    user = models.ForeignKey(User, related_name="Client")

class Subscription(models.Model):
    psyc = models.ForeignKey(Psycologist)
    clit = models.ForeignKey(Client)
