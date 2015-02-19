# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0002_auto_20150219_0930'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='owner',
            field=models.ForeignKey(related_name='blogs', to=settings.AUTH_USER_MODEL, null=True),
            preserve_default=True,
        ),
    ]
