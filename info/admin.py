from django.contrib import admin
from .models import *
# Register your models here.


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display=['user','git_url','git_username','qualification','technology','company_name','experiance','user_type']
    