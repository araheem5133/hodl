# Generated by Django 4.1.5 on 2023-02-28 03:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user", "0007_alter_activatedalgorithm_id"),
    ]

    operations = [
        migrations.AlterField(
            model_name="activatedalgorithm",
            name="long_moving_avg",
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AlterField(
            model_name="activatedalgorithm",
            name="short_moving_avg",
            field=models.PositiveIntegerField(default=0),
        ),
    ]