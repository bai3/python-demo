# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-10-21 02:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('mainsite', '0004_auto_20171021_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='pub_date',
            field=models.DateTimeField(default=datetime.datetime(2017, 10, 21, 2, 50, 7, 866363, tzinfo=utc)),
        ),
    ]