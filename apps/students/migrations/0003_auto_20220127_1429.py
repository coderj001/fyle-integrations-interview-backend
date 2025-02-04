# Generated by Django 3.1.14 on 2022-01-27 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("students", "0002_populate_data"),
    ]

    operations = [
        migrations.AlterField(
            model_name="assignment",
            name="state",
            field=models.CharField(
                choices=[
                    ("DRAFT", "DRAFT"),
                    ("SUBMITTED", "SUBMITTED"),
                    ("GRADED", "GRADED"),
                ],
                default="DRAFT",
                help_text="State of the assignment",
                max_length=9,
            ),
        ),
    ]
