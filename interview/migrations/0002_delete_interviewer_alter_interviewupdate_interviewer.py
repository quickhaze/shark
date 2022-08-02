# Generated by Django 4.0.3 on 2022-07-18 09:44

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('interview', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Interviewer',
        ),
        migrations.AlterField(
            model_name='interviewupdate',
            name='interviewer',
            field=models.ManyToManyField(to=settings.AUTH_USER_MODEL),
        ),
    ]