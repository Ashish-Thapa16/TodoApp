# Generated by Django 5.1.3 on 2024-12-08 18:55

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="task",
            name="date",
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
