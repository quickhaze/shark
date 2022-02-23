from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Role)


class DeveloperAdmin(admin.ModelAdmin):
    autocomplete_fields = ["user"]
    search_fields = ["user"]


admin.site.register(Developer, DeveloperAdmin)
