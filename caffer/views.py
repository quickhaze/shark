from django.shortcuts import render
from .models import *
from .serializer import *
from rest_framework.generics import ListAPIView, RetrieveAPIView

# Create your views here.


class ProjectDeveloperList(ListAPIView):
    queryset = ProjectDeveloper.objects.all()
    serializer_class = ProjectDeveloperSerializer


class ProjectDeveloperGet(RetrieveAPIView):
    queryset = ProjectDeveloper.objects.all()
    serializer_class = ProjectDeveloperSerializer


class RoleInProjectList(ListAPIView):
    queryset = RoleInProject.objects.all()
    serializer_class = RoleInProjectSerializer


class RoleInProjectGet(RetrieveAPIView):
    queryset = RoleInProject.objects.all()
    serializer_class = RoleInProjectSerializer


class ProjectList1(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSeializer1


class ProjectGet1(RetrieveAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSeializer1
