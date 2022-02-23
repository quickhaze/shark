from django.contrib import admin
from .models import *

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ("id", "name")
    autocomplete_fields = ["cracker"]
    search_fields = ["cracker", "name"]


class ProjectDeveloperAdmin(admin.ModelAdmin):

    list_display = (
        "id",
        "project",
        "developer",
    )

    autocomplete_fields = ["project", "developer"]
    search_fields = ["project", "developer"]


class RoleInProjectAdmin(admin.ModelAdmin):
    model = RoleInProject
    list_display = (
        "id",
        "projectdeveloper",
        "role",
        "start_date",
        "end_date",
    )
    # autocomplete_fields = ['project']
    search_fields = ["projectdeveloper", "role"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectDeveloper, ProjectDeveloperAdmin)
admin.site.register(RoleInProject, RoleInProjectAdmin)
