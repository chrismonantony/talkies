# Generated by Django 4.0.1 on 2022-05-03 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Netflix', '0011_alter_movies_stripe_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='stripe_id',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
