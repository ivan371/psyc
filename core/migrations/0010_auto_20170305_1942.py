# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 19:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_auto_20170305_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='psycologist',
            name='verified',
            field=models.CharField(choices=[('nv', 'not verified'), ('v', 'verified')], default='nv', max_length=2),
        ),
    ]
