# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-28 06:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('messaging', '0002_auto_20170628_0541'),
    ]

    operations = [
        migrations.RenameField(
            model_name='messagethread',
            old_name='when',
            new_name='when_sent',
        ),
        migrations.AddField(
            model_name='messagethread',
            name='content',
            field=models.TextField(blank=True, null=True),
        ),
    ]