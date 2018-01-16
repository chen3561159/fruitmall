# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('f_users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Goodpic',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('imgsrc', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Goodsinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gname', models.CharField(max_length=20)),
                ('intro', models.CharField(max_length=200, null=True)),
                ('unit', models.CharField(max_length=20, null=True)),
                ('stock', models.IntegerField(default=0)),
                ('isdelete', models.BooleanField(default=False)),
                ('price', models.DecimalField(null=True, max_digits=6, decimal_places=2)),
                ('details', tinymce.models.HTMLField(null=True)),
                ('click', models.IntegerField(default=0)),
                ('recom', models.IntegerField(default=0)),
                ('salenum', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Shopcar',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('gid', models.ForeignKey(to='f_goods.Goodsinfo')),
                ('uid', models.ForeignKey(to='f_users.Userinfo')),
            ],
        ),
        migrations.CreateModel(
            name='Typeinfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('tname', models.CharField(max_length=50)),
                ('goods', models.ManyToManyField(to='f_goods.Goodsinfo')),
            ],
        ),
        migrations.AddField(
            model_name='goodsinfo',
            name='gtype',
            field=models.ManyToManyField(to='f_goods.Typeinfo'),
        ),
        migrations.AddField(
            model_name='goodpic',
            name='gid',
            field=models.ForeignKey(to='f_goods.Goodsinfo'),
        ),
    ]
