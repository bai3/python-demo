# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 02:44
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0003_auto_20171021_1037'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 21, 2, 44, 2, 284520, tzinfo=utc)),
        ),
    ]