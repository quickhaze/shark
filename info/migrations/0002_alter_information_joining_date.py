# Generated by Django 3.2.12 on 2022-03-04 11:26

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="information",
            name="joining_date",
            field=models.DateField(
                default=datetime.datetime(2022, 3, 4, 16, 56, 18, 292133)
            ),
        ),
    ]
