# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-11-17 04:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('songs', '0007_auto_20171117_0403'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='last_name',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]