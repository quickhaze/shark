from django.contrib import admin
from .models import *

# Register your models here.


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    list_display = ("id", "name")

class RoleInProjectAdmin(admin.ModelAdmin):
    model = RoleInProject
    list_display = ("id", "projectdeveloper",'role','start_date','end_date',)

admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectDeveloper)
admin.site.register(RoleInProject,RoleInProjectAdmin)
