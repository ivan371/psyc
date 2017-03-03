from __future__ import unicode_literals

from django.db import models
from core.models import Psycologist
from redactor.fields import RedactorField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Article(models.Model):
    title = models.CharField(max_length=100)
    rating = models.IntegerField(default=0)

class Entry(models.Model):
    title = models.CharField(max_length=250, verbose_name=u'Title')
    content = RichTextUploadingField()
