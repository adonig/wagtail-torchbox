# -*- coding: utf-8 -*-
# Generated by Django 1.11.16 on 2019-01-21 11:46
from __future__ import unicode_literals

import json

from django.db import migrations


def populate_blogpage_authors(apps, schema_editor):
    BlogPageAuthor = apps.get_model('blog.BlogPageAuthor')
    Author = apps.get_model('people.Author')

    # Update model
    for blog_page_author in BlogPageAuthor.objects.iterator():
        if blog_page_author.author_person_page is None:
            continue

        blog_page_author.author = Author.objects.get(person_page=blog_page_author.author_person_page)
        blog_page_author.save()

    # Update revisions
    PageRevision = apps.get_model('wagtailcore.PageRevision')
    ContentType = apps.get_model('contenttypes.ContentType')
    blog_page_content_type = ContentType.objects.get(app_label='blog', model='blogpage')

    for revision in PageRevision.objects.filter(page__content_type=blog_page_content_type):
        content = json.loads(revision.content_json)

        for author in content['related_author']:
            author_obj = Author.objects.filter(person_page_id=author['author']).first()

            author['author_person_page'] = author['author']
            author['author'] = author_obj.id if author_obj is not None else None

        revision.content_json = json.dumps(content)
        revision.save()


def delete_null_authors(apps, schema_editor):
    BlogPageAuthor = apps.get_model('blog.BlogPageAuthor')
    BlogPageAuthor.objects.filter(author__isnull=True).delete()


def nooperation(apps, schema_editor):
    pass


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_blogpageauthor_author'),
        ('people', '0003_populate_authors'),
    ]

    operations = [
        migrations.RunPython(populate_blogpage_authors, nooperation),
        migrations.RunPython(delete_null_authors, nooperation),
    ]
