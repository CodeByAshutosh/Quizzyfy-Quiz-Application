# Generated by Django 4.2.7 on 2023-11-24 09:56

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("main", "0005_alter_exam_model_end_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="exam_model",
            name="end_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 24, 4, 56, 40, 438103)
            ),
        ),
        migrations.AlterField(
            model_name="exam_model",
            name="start_time",
            field=models.DateTimeField(
                default=datetime.datetime(2023, 11, 24, 4, 56, 40, 438103)
            ),
        ),
    ]
