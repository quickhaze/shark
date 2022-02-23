from distutils.command.upload import upload
from statistics import mode
import black
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from root.models import Technology
from django.core.exceptions import ValidationError

# Create your models here.


def validate_phone(phone_number):
    if phone_number.isalpha():
        # return ValidationError("Allow only 38734788")
        raise ValidationError("only Allow integer")


class Information(models.Model):
    profile = models.FileField(upload_to="profile", null=True, blank=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    technology = models.ManyToManyField(Technology)
    experiance = models.IntegerField(null=True, blank=True)
    qualification = models.TextField(null=True, blank=True)
    phone_number = models.CharField(max_length=12, validators=[validate_phone])
    joining_date = models.DateField(default=datetime.now())
    separation_date = models.DateField(null=True, blank=True)
    address = models.TextField(null=True, blank=True)

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.user.username


class College(models.Model):
    name = models.CharField(max_length=60)

    @property
    def students_count(self):
        return Student.objects.filter(course__college=self).count()

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=60)
    college = models.ForeignKey(College, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=60)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)

    def wriit(self):
        return self.course.college.name

    def __str__(self):
        return self.name
