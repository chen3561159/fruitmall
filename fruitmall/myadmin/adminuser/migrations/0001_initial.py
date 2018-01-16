# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('adminmanager', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=40)),
                ('phone', models.IntegerField(null=True)),
                ('question', models.CharField(max_length=250)),
                ('answer', models.CharField(max_length=100)),
                ('mid', models.ForeignKey(to='adminmanager.manager')),
            ],
        ),
    ]
