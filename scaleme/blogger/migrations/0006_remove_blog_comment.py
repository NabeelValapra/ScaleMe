# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0005_auto_20150226_1012'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='comment',
        ),
    ]
