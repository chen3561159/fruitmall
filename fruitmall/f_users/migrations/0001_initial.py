# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('receiver', models.CharField(max_length=20)),
                ('detaiarea', models.CharField(max_length=150)),
                ('postcode', models.IntegerField(max_length=6)),
                ('phone', models.IntegerField(max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('uname', models.CharField(max_length=20)),
                ('pwd', models.CharField(max_length=40)),
                ('phone', models.IntegerField(max_length=11, null=True)),
                ('contact', models.CharField(max_length=250, null=True)),
                ('caddress', models.IntegerField(null=True)),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='auser',
            field=models.ForeignKey(to='f_users.Userinfo'),
        ),
    ]
