# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-10-04 16:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0007_pet_breed'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='mileage',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
