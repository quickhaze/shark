from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Role)
class RoleModel(admin.ModelAdmin):
    list_display = ['id', 'role']
# admin.site.register(Role)
admin.site.register(Developer)