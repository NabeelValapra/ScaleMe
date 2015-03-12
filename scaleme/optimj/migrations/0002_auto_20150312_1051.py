# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('optimj', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addressbook',
            name='name',
        ),
        migrations.AddField(
            model_name='addressbook',
            name='email',
            field=models.EmailField(default='sample@gmail.com', max_length=75, verbose_name=b'Email ID'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addressbook',
            name='first_name',
            field=models.CharField(default='sample1', max_length=20, verbose_name=b'First Name'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='addressbook',
            name='last_name',
            field=models.CharField(default='sample2', max_length=20, verbose_name=b'Last Name'),
            preserve_default=False,
        ),
    ]
