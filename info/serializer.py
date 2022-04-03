from asyncore import read
from pyexpat import model
from rest_framework import serializers

from root.models import Technology
from .models import UserInformation
from django.contrib.auth.models import User


class UserSerailizerEmailUsername(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["email", "username"]


class UserInformationSerailizer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = [
            "technology",
            "experiance",
            "qualification",
            "phone_number",
            "joining_date",
            "separation_date",
            "address",
        ]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        l = []
        for i in data["technology"]:
            try:
                l.append(Technology.objects.get(id=i).technology)
            except Technology.DoesNotExist:
                raise serializers.ValidationError(
                    {"Technology": f"Technology {Technology} does not exixt"}
                )

        data["technology"] = l
        return data


class UserInformationProfileSerailizer(serializers.ModelSerializer):
    class Meta:
        model = UserInformation
        fields = ["profile"]


class UserSerailizer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]
