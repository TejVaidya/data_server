# Generated by Django 5.0.6 on 2024-07-09 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("user_data", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="data",
            name="valid_data",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="user",
            name="registered",
            field=models.BooleanField(default=False),
        ),
    ]
