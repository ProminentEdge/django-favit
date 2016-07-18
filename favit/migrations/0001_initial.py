# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('target_object_id', models.PositiveIntegerField()),
                ('timestamp', models.DateTimeField(auto_now_add=True, db_index=True)),
                ('target_content_type', models.ForeignKey(to='contenttypes.ContentType')),
                ('user', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-timestamp'],
                'get_latest_by': 'timestamp',
                'verbose_name': 'favorite',
                'verbose_name_plural': 'favorites',
            },
        ),
        migrations.AlterUniqueTogether(
            name='favorite',
            unique_together=set([('user', 'target_content_type', 'target_object_id')]),
        ),
    ]
