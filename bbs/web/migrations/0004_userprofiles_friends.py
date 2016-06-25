# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_article_summary'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofiles',
            name='friends',
            field=models.ManyToManyField(related_name='_userprofiles_friends_+', to='web.UserProfiles'),
        ),
    ]
