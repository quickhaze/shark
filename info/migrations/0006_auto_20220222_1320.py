# Generated by Django 3.2.12 on 2022-02-22 07:50

import datetime
from django.db import migrations, models
import info.models


class Migration(migrations.Migration):

    dependencies = [
        ("info", "0005_auto_20220222_1236"),
    ]

    operations = [
        migrations.AlterField(
            model_name="information",
            name="joining_date",
            field=models.DateField(
                default=datetime.datetime(2022, 2, 22, 13, 20, 1, 259089)
            ),
        ),
        migrations.AlterField(
            model_name="information",
            name="phone_number",
            field=models.CharField(
                max_length=12, validators=[info.models.validate_phone]
            ),
        ),
    ]
