# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-04 20:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='candidate',
            old_name='description',
            new_name='descriptions',
        ),
    ]
