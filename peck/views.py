from django.shortcuts import render
from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView


class RoleList(ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializers


class RoleGet(RetrieveAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializers


class DeveloperList(ListAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializers


class DeveloperGet(RetrieveAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializers
