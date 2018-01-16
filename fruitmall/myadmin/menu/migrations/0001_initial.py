# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Menumessage',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50)),
                ('ismenu', models.BooleanField(default=False)),
                ('isDelete', models.BooleanField(default=False)),
                ('rank', models.IntegerField(default=0, blank=True)),
                ('pid', models.ForeignKey(blank=True, to='menu.Menumessage', null=True)),
            ],
        ),
    ]
