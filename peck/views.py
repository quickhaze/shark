from rest_framework import viewsets
from django.shortcuts import render, HttpResponse
from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView


class RoleAllList(ListAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializers


class RoleGetById(RetrieveAPIView):
    queryset = Role.objects.all()
    serializer_class = RoleSerializers


class DeveloperAllList(ListAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializers


class DeveloperGetById(RetrieveAPIView):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializers


class Developer_add(viewsets.ModelViewSet):
    queryset = Developer.objects.all()
    serializer_class = DeveloperSerializers


class Role_add(viewsets.ModelViewSet):
    queryset = Role.objects.all()
    serializer_class = RoleSerializers


def RoleList(request):
    role = Role.objects.all()
    return render(request, "rolelist.html", {"role": role})


def RoleGet(requset, id):
    # import pdb;pdb.set_trace()
    role = Role.objects.get(id=id)
    devloper = role.developer_set.all()
    return render(requset, "roledetail.html", {"devloper": devloper})


def DeveloperList(request):
    devloper = Developer.objects.all()
    return render(request, "devloperlist.html", {"devloper": devloper})


def DeveloperGet(request, id):
    role = Developer.objects.get(user_id=id).role.all()
    return render(request, "devloperlist.html", {"role": role})
