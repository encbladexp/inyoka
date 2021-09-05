# Generated by Django 2.2.24 on 2021-08-22 21:54

import os

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0031_auto_20210301_0001'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='icon',
            field=models.FilePathField(blank=True, match='.*\\.png', null=True, path=os.path.join(settings.MEDIA_ROOT, 'portal/team_icons'), recursive=True, verbose_name='Group icon'),
        ),
    ]
