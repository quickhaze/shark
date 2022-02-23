from pyexpat import model
from rest_framework import serializers
from .models import Information
from django.contrib.auth.models import User


class InformationSerailizer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = [
            "profile",
            "technology",
            "experiance",
            "qualification",
            "phone_number",
            "joining_date",
            "separation_date",
            "address",
        ]


# class UserSerailizer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ["username", "first_name", "last_name"]


class UserSerailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name"]
