# Generated by Django 4.2.3 on 2023-07-23 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("todo_app", "0002_alter_todo_app_status"),
    ]

    operations = [
        migrations.AlterField(
            model_name="todo_app", name="status", field=models.CharField(max_length=50),
        ),
    ]