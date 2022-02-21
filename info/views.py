from django.shortcuts import render
from .models import Information
from .serializer import InformationSerailizer

# Create your views here.
from rest_framework import viewsets
from rest_framework.generics import CreateAPIView


class InfoCreate(viewsets.ModelViewSet):
    serializer_class = InformationSerailizer
    queryset = Information.objects.all()



