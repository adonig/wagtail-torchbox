# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-22 12:00
from __future__ import unicode_literals

import json
from functools import wraps

from django.db import migrations

from tbx.core.utils.migrations import for_each_page_revision


@for_each_page_revision('blog.BlogPage')
def rename_streamfield_to_body_in_revisions(page, content):
    content['old_body'] = content['body']
    content['body'] = content['streamfield']
    del content['streamfield']

    return content


@for_each_page_revision('blog.BlogPage')
def unrename_streamfield_to_body_in_revisions(page, content):
    content['streamfield'] = content['body']
    content['body'] = content['old_body']
    del content['old_body']

    return content


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_remove_blogindexpage_show_in_play_menu'),
    ]

    operations = [
        migrations.RunPython(rename_streamfield_to_body_in_revisions, unrename_streamfield_to_body_in_revisions),
        migrations.RenameField(
            model_name='blogpage',
            old_name='streamfield',
            new_name='body',
        ),
    ]