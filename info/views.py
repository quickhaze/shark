from dataclasses import fields
from functools import partial
from typing import Dict
from django.http import Http404
from django.shortcuts import redirect, render
from django.urls import reverse
from .models import UserInformation
from .serializer import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from root.models import Technology


class InfoCreate(APIView):
    def get(self, request):
        data = User.objects.get(id=request.user.id)
        data1 = UserInformation.objects.get(id=request.user.UserInformation.id)
        serializer = UserSerailizer(data)
        serializer1 = UserInformationSerailizer(data1)
        return Response({"user": serializer.data, "profile": serializer1.data})

    def post(self, request):
        new_data = request.data.copy()
        serializer1 = UserSerailizer(data=new_data, instance=request.user, partial=True)
        serializer = UserInformationSerailizer(
            data=new_data, instance=request.user.UserInformation, partial=True
        )
        if serializer.is_valid(raise_exception=True) and serializer1.is_valid(
            raise_exception=True
        ):
            serializer.save()
            serializer1.save()
            return Response(
                {
                    "message": "updated",
                    "data": serializer.data,
                    "user_details": serializer1.data,
                },
                status=201,
            )
        return Response(
            {"info": serializer.errors, "user": serializer1.errors}, status=201
        )


class ProfileCreate(APIView):
    def get(self, request):
        data = UserInformation.objects.get(id=request.user.UserInformation.id)
        serializer = UserInformationProfileSerailizer(data)
        return Response(serializer.data)

    def post(self, request):
        serializer = UserInformationProfileSerailizer(
            data=request.data, instance=request.user.UserInformation
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"update_profile_file": serializer.data}, status=201)


class EmailUsernameOnly(APIView):
    def get(self, request):
        data = User.objects.get(id=request.user.id)
        serializer = UserSerailizerEmailUsername(data)
        return Response(serializer.data, status=201)
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView, CreateView
# from django.views.generic
from .models import Documents
from django.views import View
from .forms import DocumetsForm
Any = object
from django.contrib.auth.mixins import LoginRequiredMixin

class Profile(LoginRequiredMixin, DetailView):
    model = User
    template_name = 'user-profile.html'

    # def get_context_data(self, **kwargs: Any):
    #     ctx = super().get_context_data(**kwargs)
    #     return ctx

class DocUpload(View):
    def post(self, request,*args, **kwargs):
        form = DocumetsForm(request.POST, request.FILES)
        if form.is_valid():
            Documents.objects.create(user_info = request.user.userinformation, **form.cleaned_data)
        return redirect(reverse('root:index'))