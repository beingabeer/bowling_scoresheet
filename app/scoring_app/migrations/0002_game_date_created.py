# Generated by Django 3.0.5 on 2020-04-25 02:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('scoring_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='date_created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
