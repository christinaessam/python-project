# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-02-28 18:17
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newsweb', '0004_auto_20160228_1812'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_image',
        ),
    ]
