# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('menu', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='menumessage',
            name='pid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.SET_NULL, blank=True, to='menu.Menumessage', null=True),
        ),
    ]
