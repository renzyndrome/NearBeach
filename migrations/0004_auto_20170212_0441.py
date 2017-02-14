# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-12 04:41
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('NearBeach', '0003_auto_20170212_0434'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tasks',
            name='task_assigned_to',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]