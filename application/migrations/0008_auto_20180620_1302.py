# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-20 13:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0007_auto_20180619_1447'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='childcareaddress',
            name='address_to_be_provided',
        ),
        migrations.AddField(
            model_name='nannyapplication',
            name='address_to_be_provided',
            field=models.NullBooleanField(default=None),
        ),
    ]
