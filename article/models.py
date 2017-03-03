from __future__ import unicode_literals

from django.db import models
from core.models import Psycologist, User
from redactor.fields import RedactorField
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField

class Entry(models.Model):
    user = models.ForeignKey(User)
    title = models.CharField(max_length=250, verbose_name=u'Title')
    content = RichTextUploadingField()
