# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-22 15:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_remove_blogpage_colour'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpage',
            name='body_word_count',
            field=models.PositiveIntegerField(editable=False, null=True),
        ),
    ]