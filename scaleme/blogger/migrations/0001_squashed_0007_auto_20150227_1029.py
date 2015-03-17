# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    replaces = [(b'blogger', '0001_initial'), (b'blogger', '0002_auto_20150219_0930'), (b'blogger', '0003_auto_20150219_1107'), (b'blogger', '0004_auto_20150225_0807'), (b'blogger', '0005_auto_20150226_1012'), (b'blogger', '0006_remove_blog_comment'), (b'blogger', '0007_auto_20150227_1029')]

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('owner', models.ForeignKey(related_name='blogs', to=settings.AUTH_USER_MODEL, null=True)),
                ('likes', models.IntegerField(default='1')),
                ('comment', models.CharField(default='Initial Comment', max_length=200)),
            ],
            options={
                'db_table': 'scaleme_blogs',
            },
            bases=(models.Model,),
        ),
    ]
