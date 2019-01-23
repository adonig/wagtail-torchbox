# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-15 21:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailsearchpromotions', '0002_capitalizeverbose'),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('wagtailcore', '0040_page_draft_title'),
        ('torchbox', '0107_move_services_into_new_app'),
    ]

    database_operations = [
        migrations.AlterModelTable('WorkIndexPage', 'work_workindexpage'),
        migrations.AlterModelTable('WorkPage', 'work_workpage'),
        migrations.AlterModelTable('WorkPageAuthor', 'work_workpageauthor'),
        migrations.AlterModelTable('WorkPageScreenshot', 'work_workpagescreenshot'),
        migrations.AlterModelTable('WorkPageTagSelect', 'work_workpagetagselect'),
    ]

    state_operations = [
        migrations.RemoveField(
            model_name='workindexpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='workpage',
            name='feed_image',
        ),
        migrations.RemoveField(
            model_name='workpage',
            name='homepage_image',
        ),
        migrations.RemoveField(
            model_name='workpage',
            name='page_ptr',
        ),
        migrations.RemoveField(
            model_name='workpageauthor',
            name='author',
        ),
        migrations.RemoveField(
            model_name='workpageauthor',
            name='page',
        ),
        migrations.RemoveField(
            model_name='workpagescreenshot',
            name='image',
        ),
        migrations.RemoveField(
            model_name='workpagescreenshot',
            name='page',
        ),
        migrations.RemoveField(
            model_name='workpagetagselect',
            name='page',
        ),
        migrations.RemoveField(
            model_name='workpagetagselect',
            name='tag',
        ),
        migrations.DeleteModel(
            name='WorkIndexPage',
        ),
        migrations.DeleteModel(
            name='WorkPage',
        ),
        migrations.DeleteModel(
            name='WorkPageAuthor',
        ),
        migrations.DeleteModel(
            name='WorkPageScreenshot',
        ),
        migrations.DeleteModel(
            name='WorkPageTagSelect',
        ),
    ]

    operations = [
        migrations.SeparateDatabaseAndState(
            database_operations=database_operations,
            state_operations=state_operations,
        )
    ]
