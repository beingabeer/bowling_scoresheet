# Generated by Django 3.0.5 on 2020-04-26 14:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('scoring_app', '0003_remove_game_is_over'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='frame',
            name='roll_four',
        ),
        migrations.RemoveField(
            model_name='frame',
            name='roll_one',
        ),
        migrations.RemoveField(
            model_name='frame',
            name='roll_three',
        ),
        migrations.RemoveField(
            model_name='frame',
            name='roll_two',
        ),
        migrations.AddField(
            model_name='frame',
            name='frame_is_active',
            field=models.BooleanField(default=False),
        ),
        migrations.CreateModel(
            name='Roll',
            fields=[
                ('roll_id', models.AutoField(primary_key=True, serialize=False)),
                ('roll_one', models.IntegerField(default=0)),
                ('roll_two', models.IntegerField(default=0)),
                ('roll_three', models.IntegerField(default=0)),
                ('roll_four', models.IntegerField(default=0)),
                ('frame_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='scoring_app.Frame')),
            ],
        ),
    ]
