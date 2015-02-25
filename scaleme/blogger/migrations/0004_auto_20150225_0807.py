# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0003_auto_20150219_1107'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='comment',
            field=models.CharField(default='Migration Comments', max_length=200),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blog',
            name='likes',
            field=models.IntegerField(default='1'),
            preserve_default=False,
        ),
    ]
