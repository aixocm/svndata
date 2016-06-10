# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Business',
            fields=[
                ('nid', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=16)),
                ('name1', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('hostname', models.CharField(max_length=32)),
                ('business', models.ForeignKey(to='app01.Business')),
            ],
        ),
        migrations.CreateModel(
            name='Somthing',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('c1', models.CharField(max_length=16)),
                ('c2', models.CharField(max_length=16)),
                ('c3', models.CharField(max_length=16)),
                ('c4', models.CharField(max_length=16)),
                ('color', models.ForeignKey(to='app01.Color')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('user_type', models.IntegerField(default=1, choices=[(1, b'f'), (2, b'fdg')])),
                ('name', models.CharField(unique=True, max_length=32, verbose_name=b'\xe5\xa7\x93\xe5\x90\x8d', db_column=b'KJH')),
                ('email', models.EmailField(max_length=32, null=True)),
                ('email2', models.EmailField(default=b'1755897532@qq.com', max_length=32)),
                ('ip', models.GenericIPAddressField(null=True, protocol=b'ipv4', blank=True)),
                ('img', models.ImageField(null=True, upload_to=b'upload', blank=True)),
                ('ctime', models.DateTimeField(auto_now=True)),
                ('uptime', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
