# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-21 12:49
from __future__ import unicode_literals

from django.db import migrations
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_remove_blogpage_author_left'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpageauthor',
            name='page',
            field=modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='authors', to='blog.BlogPage'),
        ),
    ]
