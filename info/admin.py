from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(UserInformation)
class InformationAdmin(admin.ModelAdmin):
    list_display = [
        "user",
    ]


@admin.register(Documents)
class InformationAdmin(admin.ModelAdmin):
    list_display = ["user_info", "doc"]


@admin.register(Address)
class InformationAdmin(admin.ModelAdmin):
    ...


admin.site.register(DailyUpdate)
