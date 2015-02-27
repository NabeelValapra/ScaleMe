# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0006_remove_blog_comment'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Comment',
        ),
        migrations.AddField(
            model_name='blog',
            name='comment',
            field=models.CharField(default='Initial Comment', max_length=200),
            preserve_default=False,
        ),
    ]
