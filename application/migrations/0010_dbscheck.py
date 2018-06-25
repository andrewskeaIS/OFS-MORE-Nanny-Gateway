# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-25 16:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0009_childcaretraining_firstaidtraining'),
    ]

    operations = [
        migrations.CreateModel(
            name='DbsCheck',
            fields=[
                ('dbs_id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('dbs_number', models.CharField(max_length=100)),
                ('convictions', models.NullBooleanField(default=None)),
                ('application_id', models.ForeignKey(db_column='application_id', on_delete=django.db.models.deletion.CASCADE, to='application.NannyApplication')),
            ],
            options={
                'db_table': 'DBS_CHECK',
            },
        ),
    ]
