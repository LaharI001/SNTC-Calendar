# -*- coding: utf-8 -*-
# Generated by Django 1.11.24 on 2019-09-27 11:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_auto_20190927_1713'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='club',
            field=models.CharField(help_text='the name of your club', max_length=100, null=True),
        ),
    ]
