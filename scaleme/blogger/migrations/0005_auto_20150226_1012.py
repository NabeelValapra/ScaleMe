# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogger', '0004_auto_20150225_0807'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('comment', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'scaleme_comments',
            },
            bases=(models.Model,),
        ),
        migrations.AlterField(
            model_name='blog',
            name='comment',
            field=models.ForeignKey(to='blogger.Comment'),
            preserve_default=True,
        ),
    ]
