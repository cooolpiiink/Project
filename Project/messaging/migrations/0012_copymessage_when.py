# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 09:15
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0011_auto_20170630_0837'),
    ]

    operations = [
        migrations.AddField(
            model_name='copymessage',
            name='when',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
