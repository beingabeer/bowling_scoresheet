# Generated by Django 3.0.5 on 2020-04-24 17:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scoring_app', '0007_auto_20200424_1615'),
    ]

    operations = [
        migrations.AlterField(
            model_name='frame',
            name='frame_no',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9), (10, 10)], unique=True),
        ),
    ]
