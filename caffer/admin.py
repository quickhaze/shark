from django.contrib import admin
from .models import *

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ("id", "name")


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectDeveloper)
admin.site.register(RoleInProject)
