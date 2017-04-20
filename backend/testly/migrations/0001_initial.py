# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-17 10:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestRun',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(0, 'Pending'), (1, 'Running'), (2, 'Success'), (3, 'Failure')], default=0, editable=False)),
                ('task_id', models.CharField(blank=True, default='', max_length=36, verbose_name='Django RQ Task ID')),
                ('requested_by', models.CharField(max_length=50, verbose_name='Requester')),
                ('path', models.CharField(default='.', help_text='Path relative to tests directory', max_length=4096)),
                ('environment', models.SmallIntegerField(verbose_name='Environment ID')),
                ('interface', models.SmallIntegerField(choices=[(0, 'SOAP API')], default=0, help_text='Interface between the test executor web application and the Python test runner')),
                ('logs', models.TextField(blank=True, default='')),
                ('created_at', models.DateTimeField(auto_now_add=True, db_index=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, db_index=True, null=True)),
            ],
        ),
    ]