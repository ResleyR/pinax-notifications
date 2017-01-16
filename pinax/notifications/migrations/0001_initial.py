# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-03-19 11:36
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='NoticeQueueBatch',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pickled_data', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NoticeSetting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('medium', models.CharField(choices=[(0, 'email')], max_length=1, verbose_name='medium')),
                ('send', models.BooleanField(default=False, verbose_name='send')),
                ('scoping_object_id', models.PositiveIntegerField(blank=True, null=True)),
            ],
            options={
                'verbose_name': 'notice setting',
                'verbose_name_plural': 'notice settings',
            },
        ),
        migrations.CreateModel(
            name='NoticeType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=40, verbose_name='label')),
                ('display', models.CharField(max_length=50, verbose_name='display')),
                ('description', models.CharField(max_length=100, verbose_name='description')),
                ('default', models.IntegerField(verbose_name='default')),
            ],
            options={
                'verbose_name_plural': 'notice types',
                'verbose_name': 'notice type',
            },
        ),
        migrations.AddField(
            model_name='noticesetting',
            name='notice_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pinax_notifications.NoticeType', verbose_name='notice type'),
        ),
        migrations.AddField(
            model_name='noticesetting',
            name='scoping_content_type',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.ContentType'),
        ),
        migrations.AddField(
            model_name='noticesetting',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AlterUniqueTogether(
            name='noticesetting',
            unique_together=set([('user', 'notice_type', 'medium', 'scoping_content_type', 'scoping_object_id')]),
        ),
    ]
