# Generated by Django 2.0.6 on 2018-10-06 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('friends', '0002_game'),
    ]

    operations = [
        migrations.AddField(
            model_name='game',
            name='is_hidden',
            field=models.BooleanField(default=False),
        ),
    ]