from pyexpat import model
from statistics import mode
import black
from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
from root.models import InitModel, Technology
from django.core.exceptions import ValidationError
from datetime import date
from projects.models import Project

# Create your models here.


def validate_phone(phone_number):
    if phone_number.isalpha():
        # return ValidationError("Allow only 38734788")
        raise ValidationError("only Allow integer")


class UserInformation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.FileField(
        upload_to="profile_image",
        null=True,
        blank=True,
        default="profile_image/viber.png",
    )
    joining_date = models.DateField(default=datetime.now)
    separation_date = models.DateField(null=True, blank=True)
    technologies = models.ManyToManyField(Technology)
    experience = models.IntegerField(null=True, blank=True)
    qualification = models.TextField(null=True, blank=True)
    bio = models.TextField(null=True, blank=True)
    dob = models.DateField(blank=True, null=True)
    position = models.CharField(max_length=200, null=True, blank=True)
    about_me = models.TextField(default="About me")

    class Meta:
        ordering = ["-id"]

    def __str__(self):
        return self.user.username


class Address(models.Model):
    user_info = models.OneToOneField(UserInformation, on_delete=models.CASCADE)
    address_line_1 = models.CharField(max_length=500, null=True, blank=True)
    address_line_2 = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    zip_code = models.IntegerField()
    phone_number = models.CharField(max_length=16, validators=[validate_phone])

    def __str__(self):
        return self.user_info.user.username


class Documents(models.Model):
    user_info = models.ForeignKey(UserInformation, on_delete=models.CASCADE)
    name = models.CharField(max_length=50, null=True, blank=True)
    doc = models.FileField(upload_to="doc", null=True, blank=True)

    def __str__(self):
        return self.user_info.user.username


class DailyUpdate(InitModel):
    date = models.DateField(blank=True, null=True)
    project = models.ForeignKey(
        Project,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="daily_updates",
    )
    user = models.ForeignKey(
        User,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="daily_updates",
    )
    detail = models.TextField()
    chat_id = models.CharField(null=True, blank=True, max_length=100)
    
    class Meta:
        ordering = ("date",)

    def __str__(self) -> str:
        return f"{self.detail}"
