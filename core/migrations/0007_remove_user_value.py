# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 18:36
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0006_auto_20170305_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='value',
        ),
    ]