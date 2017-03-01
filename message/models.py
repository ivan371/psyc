from __future__ import unicode_literals

from django.db import models
from core.models import Psycologist, Client, User

class Chat(models.Model):

    psycologist = models.ForeignKey(Psycologist, related_name="psycologist")
    client = models.ForeignKey(Client, related_name="client")

class Message(models.Model):

    user = models.ForeignKey(User)
    char = models.ForeignKey(Chat)
    content = models.TextField()
