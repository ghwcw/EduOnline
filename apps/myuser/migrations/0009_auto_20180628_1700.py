# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-06-28 17:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myuser', '0008_auto_20180628_1557'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='nick_name',
            field=models.CharField(blank=True, max_length=20, null=True, verbose_name='昵称'),
        ),
    ]
