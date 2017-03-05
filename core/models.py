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
    PROF_CHOISE = (
        ('0', 'client'),
        ('1', 'psycologist'),
    )
    prof = models.CharField(max_length=2, choices=PROF_CHOISE, default=0)
    def is_psycologist(self):
        if self.prof == '1':
            return True
        else:
            return False

class Psycologist(models.Model):
    user = models.OneToOneField(User, related_name="psycologist")
    NOT_VERIFIED = 'nv'
    VERIFIED = 'v'
    VERIFIED_CHOISE = (
        (NOT_VERIFIED, 'not verified'),
        (VERIFIED, 'verified'),
    )
    verified = models.CharField(max_length=2, choices=VERIFIED_CHOISE, default=NOT_VERIFIED)
    document = models.ImageField(upload_to='document', blank=True, null=True)


class Client(models.Model):
    user = models.OneToOneField(User, related_name="client")

class Subscription(models.Model):
    psyc = models.ForeignKey(Psycologist)
    clit = models.ForeignKey(Client)
