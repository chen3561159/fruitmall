# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('f_users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='address',
            name='phone',
            field=models.BigIntegerField(),
        ),
        migrations.AlterField(
            model_name='address',
            name='postcode',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='userinfo',
            name='phone',
            field=models.IntegerField(null=True),
        ),
    ]
