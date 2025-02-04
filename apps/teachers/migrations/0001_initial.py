# Generated by Django 3.1.14 on 2022-01-27 13:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("internal", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Teacher",
            fields=[
                ("id", models.AutoField(primary_key=True, serialize=False)),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, help_text="Created at"),
                ),
                (
                    "updated_at",
                    models.DateTimeField(auto_now=True, help_text="Updated at"),
                ),
                (
                    "user",
                    models.OneToOneField(
                        help_text="Reference to User model",
                        on_delete=django.db.models.deletion.CASCADE,
                        to="internal.user",
                    ),
                ),
            ],
            options={
                "db_table": "teachers",
            },
        ),
    ]
