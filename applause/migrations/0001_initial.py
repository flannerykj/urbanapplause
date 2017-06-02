# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-05-19 17:12
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import geoposition.fields
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('taggit', '0002_auto_20150616_2121'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('talent', '0007_talent_talent_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplauseGF',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('location', geoposition.fields.GeopositionField(max_length=42)),
                ('comments', models.CharField(max_length=400)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ApplauseMS',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pub_date', models.DateTimeField(auto_now_add=True)),
                ('location', geoposition.fields.GeopositionField(max_length=42)),
                ('comments', models.CharField(max_length=400)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GenreTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applause.ApplauseMS')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applause_genretag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='InstrumentTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applause.ApplauseMS')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applause_instrumenttag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MediumTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applause.ApplauseGF')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applause_mediumtag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='StyleTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content_object', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='applause.ApplauseGF')),
                ('tag', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applause_styletag_items', to='taggit.Tag')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='applausems',
            name='genres',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='applause.GenreTag', to='taggit.Tag', verbose_name='genres'),
        ),
        migrations.AddField(
            model_name='applausems',
            name='instruments',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='applause.InstrumentTag', to='taggit.Tag', verbose_name='instruments'),
        ),
        migrations.AddField(
            model_name='applausems',
            name='talent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talent.Talent'),
        ),
        migrations.AddField(
            model_name='applausems',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='applausegf',
            name='style',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='applause.StyleTag', to='taggit.Tag', verbose_name='style'),
        ),
        migrations.AddField(
            model_name='applausegf',
            name='talent',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='talent.Talent'),
        ),
        migrations.AddField(
            model_name='applausegf',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
