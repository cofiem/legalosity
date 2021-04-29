# Generated by Django 2.1.2 on 2018-10-21 06:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('unravel', '0002_document'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentTag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('archived_date', models.DateTimeField(blank=True, null=True)),
                ('title', models.CharField(help_text='Tag title', max_length=300, unique=True)),
                ('name', models.SlugField(help_text='Unique tag slug', max_length=100, unique=True)),
                ('description', models.TextField(blank=True, help_text='Tag description', null=True)),
                ('archived_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unravel_documenttag_archived', related_query_name='unravel_documenttag_archivers', to=settings.AUTH_USER_MODEL)),
                ('created_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unravel_documenttag_created', related_query_name='unravel_documenttag_creators', to=settings.AUTH_USER_MODEL)),
                ('documents', models.ManyToManyField(help_text='Documents assigned this tag', related_name='tags', to='unravel.Document')),
                ('updated_user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='unravel_documenttag_updated', related_query_name='unravel_documenttag_updaters', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Document Tag',
                'verbose_name_plural': 'Document Tags',
            },
        ),
    ]