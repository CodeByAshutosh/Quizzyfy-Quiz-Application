# Generated by Django 4.2 on 2023-12-01 22:50

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("prof", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="score",
            name="exam",
        ),
        migrations.RemoveField(
            model_name="score",
            name="user",
        ),
        migrations.DeleteModel(
            name="Exam",
        ),
        migrations.DeleteModel(
            name="Score",
        ),
    ]
