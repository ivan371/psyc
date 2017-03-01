from __future__ import unicode_literals

from django.db import models
from core.models import Psycologist

class Article(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)


class Contentable(models.Model):
    article = models.ForeignKey(Article)

    class Meta:
		abstract = True


class Textart(Contentable):

    text = models.TextField()

class Videoart(Contentable):

    pass

class Audioart(Contentable):

    pass

class Imageart(Contentable):

    img = models.ImageField(upload_to='post_img', blank=True, null=True)
