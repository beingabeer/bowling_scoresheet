# Generated by Django 3.0.5 on 2020-04-27 01:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring_app', '0005_auto_20200426_1802'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frame',
            name='roll_one',
            field=models.PositiveIntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AlterField(
            model_name='frame',
            name='roll_two',
            field=models.IntegerField(choices=[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], default=0),
        ),
        migrations.AlterField(
            model_name='player',
            name='player_name',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]