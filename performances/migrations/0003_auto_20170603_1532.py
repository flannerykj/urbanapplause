# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-06-03 19:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('performances', '0002_auto_20170603_1346'),
    ]

    operations = [
        migrations.AlterField(
            model_name='performance',
            name='musicians',
            field=models.ManyToManyField(null=True, through='performances.Participation', to='musicians.Musician'),
        ),
    ]