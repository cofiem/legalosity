# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-28 21:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='document',
            name='document_type',
            field=models.ForeignKey(help_text='The type of this document.', on_delete=django.db.models.deletion.PROTECT, related_name='documents', to='core.DocumentType'),
        ),
    ]