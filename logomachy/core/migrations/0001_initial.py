# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 04:33
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='The date the record was created.')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='The date the record was last modified.')),
                ('name', models.SlugField(help_text='A unique, possibly generated, name for the document.', max_length=100, unique=True)),
                ('title', models.CharField(help_text='The human-readable name of the document.', max_length=1000)),
                ('author', models.CharField(help_text='The person, company, or other entity that created this document.', max_length=1000)),
                ('document_date', models.DateField(help_text='The date the document was retrieved or last updated.')),
                ('source_url', models.URLField(blank=True, help_text='The website this document was sourced from (optional).', max_length=2000, null=True)),
                ('document_version', models.CharField(blank=True, help_text='The version of this document (optional).', max_length=100, null=True)),
                ('document_content', models.TextField(help_text='The content for this document.')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DocumentType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True, help_text='The date the record was created.')),
                ('modified_date', models.DateTimeField(auto_now=True, help_text='The date the record was last modified.')),
                ('name', models.CharField(help_text='The name of the document type.', max_length=100)),
                ('description', models.CharField(help_text='The description of the document type.', max_length=2000)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='document',
            name='document_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='documents', to='core.DocumentType'),
        ),
    ]
