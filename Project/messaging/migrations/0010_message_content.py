# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-30 08:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0009_auto_20170630_0823'),
    ]

    operations = [
        migrations.AddField(
            model_name='message',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]