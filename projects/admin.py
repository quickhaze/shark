from atexit import register
from django.contrib import admin
from .models import Project, AssignedProject, ProjectDocument
from .models import Repository, Credentials

# Register your models here.

admin.site.register(Project)
admin.site.register(Repository)
admin.site.register(Credentials)
admin.site.register(AssignedProject)
admin.site.register(ProjectDocument)
