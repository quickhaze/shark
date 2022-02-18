from rest_framework import serializers
from .models import Information


class InformationSerailizer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")
    class Meta:
        model = Information
        fields = "__all__"
