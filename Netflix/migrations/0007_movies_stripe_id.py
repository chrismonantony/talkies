# Generated by Django 4.0.1 on 2022-05-03 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Netflix', '0006_remove_movies_users_movies_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='movies',
            name='stripe_id',
            field=models.CharField(default='prod_LcUG504bMf1NGj', max_length=50),
        ),
    ]
