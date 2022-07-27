# Generated by Django 4.0.3 on 2022-07-18 08:30

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('resume', models.FileField(upload_to='media')),
                ('date', models.DateField(default=datetime.datetime.today)),
            ],
        ),
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=35)),
                ('email', models.EmailField(max_length=254)),
                ('phone1', models.CharField(max_length=12)),
                ('phone2', models.CharField(blank=True, max_length=12, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female'), ('O', 'Other')], max_length=1)),
                ('profile', models.CharField(choices=[('python', 'Python Developer'), ('REACT', 'React Developer'), ('HR', 'Human Resource'), ('BDE', 'Business Development Executive')], default='python', max_length=6)),
                ('source', models.CharField(choices=[('IN', 'Linkedin'), ('INDEED', 'Indeed'), ('APNA', 'Apna'), ('NAUKRI', 'Naukri'), ('REF', 'Reference'), ('SOCIAL', 'Social Media'), ('CONSULTANCY', 'Consultancy'), ('OTHER', 'Other')], max_length=11)),
            ],
        ),
        migrations.CreateModel(
            name='Interviewer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=12)),
                ('technology', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('job_domain', models.CharField(max_length=15)),
                ('job_openings', models.CharField(max_length=15)),
            ],
        ),
        migrations.CreateModel(
            name='Qualification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('graduation_type', models.CharField(choices=[('UG', 'UG'), ('PG', 'PG'), ('PHD', 'PHD'), ('diploma', 'Diploma')], max_length=7)),
                ('degree', models.CharField(max_length=20)),
                ('year', models.CharField(max_length=4)),
                ('percentage', models.FloatField(max_length=4)),
                ('institue', models.CharField(max_length=35)),
                ('candidate', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.candidate')),
            ],
        ),
        migrations.CreateModel(
            name='InterviewUpdate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interview_stage', models.CharField(choices=[('first', 'First Round'), ('second', 'Second Round'), ('final', 'Final Round')], max_length=6)),
                ('remark', models.TextField()),
                ('datetime', models.DateTimeField(auto_now_add=True)),
                ('application', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='interview_update', to='interview.application')),
                ('follow_up', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='interview.interviewupdate')),
                ('interviewer', models.ManyToManyField(to='interview.interviewer')),
            ],
        ),
        migrations.AddField(
            model_name='application',
            name='applying_job',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='interview.job'),
        ),
        migrations.AddField(
            model_name='application',
            name='candidate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='applications', to='interview.candidate'),
        ),
    ]