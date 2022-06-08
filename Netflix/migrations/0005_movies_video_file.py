# Generated by Django 4.0.1 on 2022-04-27 13:56

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Netflix', '0004_alter_movies_duration'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='video_file',
            field=models.FileField(null=True, upload_to='videos', validators=[django.core.validators.FileExtensionValidator(allowed_extensions=['MOV', 'avi', 'mp4', 'webm', 'mkv'])]),
        ),
    ]
