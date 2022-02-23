from django.contrib import admin
from .models import *

# Register your models here.


@admin.register(Information)
class InformationAdmin(admin.ModelAdmin):
    list_display = [
        "user",
    ]


admin.site.register(Course)


class StudenAdmin(admin.ModelAdmin):
    list_display = ["name", "course", "wriit"]


class CollegeAdmin(admin.ModelAdmin):
    list_display = ["name", "students_count"]


admin.site.register(College, CollegeAdmin)
admin.site.register(Student, StudenAdmin)
