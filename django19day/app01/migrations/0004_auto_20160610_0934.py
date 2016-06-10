# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0003_auto_20160609_2047'),
    ]

    operations = [
        migrations.CreateModel(
            name='User_New',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('username', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='UserGroup_New',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('caption', models.CharField(max_length=64)),
            ],
        ),
        migrations.AddField(
            model_name='user_new',
            name='user_group',
            field=models.ForeignKey(to='app01.UserGroup_New'),
        ),
    ]
