# Generated by Django 1.11.25 on 2019-10-27 18:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0013_auto_20190415_0016'),
    ]

    operations = [
        migrations.AlterField(
            model_name='attachment',
            name='file',
            field=models.FileField(max_length=250, upload_to='forum/attachments/temp'),
        ),
    ]
