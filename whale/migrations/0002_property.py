# Generated by Django 4.0.1 on 2022-01-08 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('whale', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Property',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.IntegerField()),
            ],
        ),
    ]
