# Generated by Django 3.0.5 on 2020-04-24 16:15

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring_app', '0006_auto_20200424_1601'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frame',
            name='frame_no',
            field=models.IntegerField(unique=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(1)]),
        ),
    ]
