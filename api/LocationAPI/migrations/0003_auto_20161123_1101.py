# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-11-23 05:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('LocationAPI', '0002_auto_20161123_1051'),
    ]

    operations = [
        migrations.RenameField(
            model_name='locationofuser',
            old_name='longtude',
            new_name='longitude',
        ),
    ]
