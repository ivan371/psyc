# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-06 11:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_user_prof'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='prof',
            field=models.CharField(choices=[('0', 'client'), ('1', 'psycologist')], default=0, max_length=2),
        ),
    ]
