# Generated by Django 3.0.5 on 2020-04-27 23:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('scoring_app', '0006_auto_20200427_0109'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='game',
            name='final_score',
        ),
    ]
