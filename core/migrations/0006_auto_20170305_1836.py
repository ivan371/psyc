# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-05 18:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_remove_psycologist_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='client',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Client', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='psycologist',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Psycologist', to=settings.AUTH_USER_MODEL),
        ),
    ]
