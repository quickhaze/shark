from django.shortcuts import render, HttpResponse
from .serializers import *
from .models import *
from rest_framework.generics import ListAPIView
from rest_framework.generics import RetrieveAPIView


# class RoleList(ListAPIView):
#     queryset = Role.objects.all()
#     serializer_class = RoleSerializers


# class RoleGet(RetrieveAPIView):
#     queryset = Role.objects.all()
#     serializer_class = RoleSerializers


# class DeveloperList(ListAPIView):
#     queryset = Developer.objects.all()
#     serializer_class = DeveloperSerializers


# class DeveloperGet(RetrieveAPIView):
#     queryset = Developer.objects.all()
#     serializer_class = DeveloperSerializers


def roleList(request):
    role = Role.objects.all()
    return render(request, "rolelist.html", {"role": role})


def roleGet(requset, id):
    # import pdb;pdb.set_trace()
    role = Role.objects.get(id=id)
    devloper = role.developer_set.all()
    return render(requset, "roledetail.html", {"devloper": devloper})


def developerList(request):
    devloper = Developer.objects.all()
    return render(request, "devloperlist.html", {"devloper": devloper})


def developerGet(request, id):
    role = Developer.objects.get(user_id=id).role.all()
    return render(request, "devloperlist.html", {"role": role})
