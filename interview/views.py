from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JobsSerializer
from .models import Job

class JobsViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobsSerializer