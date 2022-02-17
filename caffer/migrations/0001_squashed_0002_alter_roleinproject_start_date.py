# Generated by Django 3.2.12 on 2022-02-17 07:16

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    replaces = [
        ("caffer", "0001_initial"),
        ("caffer", "0002_alter_roleinproject_start_date"),
    ]

    initial = True

    dependencies = [
        ("peck", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Project",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "name",
                    models.CharField(
                        help_text="The name of the project", max_length=200
                    ),
                ),
                (
                    "cracker",
                    models.ForeignKey(
                        help_text="The name of the developer who cracked the interview",
                        max_length=200,
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="project_cracker",
                        to="peck.developer",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="ProjectDeveloper",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "developer",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="peck.developer"
                    ),
                ),
                (
                    "project",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="caffer.project"
                    ),
                ),
            ],
            options={
                "ordering": ("created_at",),
            },
        ),
        migrations.CreateModel(
            name="RoleInProject",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "start_date",
                    models.DateField(
                        default=datetime.datetime(2022, 2, 17, 12, 32, 25, 339656)
                    ),
                ),
                ("end_date", models.DateField(blank=True, null=True)),
                (
                    "projectdeveloper",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        to="caffer.projectdeveloper",
                    ),
                ),
                (
                    "role",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT, to="peck.role"
                    ),
                ),
            ],
            options={
                "ordering": ("created_at",),
            },
        ),
        migrations.AddField(
            model_name="projectdeveloper",
            name="role_in_project",
            field=models.ManyToManyField(
                through="caffer.RoleInProject", to="peck.Role"
            ),
        ),
        migrations.AddField(
            model_name="project",
            name="developer",
            field=models.ManyToManyField(
                help_text="The name of the developers contributed to the project on the project",
                through="caffer.ProjectDeveloper",
                to="peck.Developer",
                verbose_name="developers",
            ),
        ),
    ]
