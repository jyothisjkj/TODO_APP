# Generated by Django 4.2.3 on 2023-07-23 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo_app", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo_app",
            name="status",
            field=models.BooleanField(default=False),
        ),
    ]
