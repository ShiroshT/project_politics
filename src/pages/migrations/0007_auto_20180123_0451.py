# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-23 04:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0006_auto_20180123_0439'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='candidate',
            options={'ordering': ['-timestamp', 'id_candidate']},
        ),
        migrations.AlterOrderWithRespectTo(
            name='candidate',
            order_with_respect_to=None,
        ),
    ]