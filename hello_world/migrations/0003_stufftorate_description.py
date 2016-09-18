# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello_world', '0002_stufftorate_color'),
    ]

    operations = [
        migrations.AddField(
            model_name='stufftorate',
            name='description',
            field=models.TextField(default='This is my long text description of the field for this thing.'),
            preserve_default=False,
        ),
    ]
