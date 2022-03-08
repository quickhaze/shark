from functools import partial
from django.http import Http404
from django.shortcuts import render
from .models import Information
from .serializer import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from root.models import Technology


class InfoCreate(APIView):
    def get(self, request):
        data = User.objects.get(id=request.user.id)
        data1 = Information.objects.get(id=request.user.information.id)
        serializer = UserSerailizer(data)
        serializer1 = InformationSerailizer(data1)
        return Response({"user": serializer.data, "profile": serializer1.data})

    def post(self, request):
        import pdb

        pdb.set_trace()
        new_data = request.data.copy()
        serializer1 = UserSerailizer(data=new_data, instance=request.user, partial=True)
        serializer = InformationSerailizer(
            data=new_data, instance=request.user.information, partial=True
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
        data = Information.objects.get(id=request.user.information.id)
        serializer = InformationProfileSerailizer(data)
        return Response(serializer.data)

    def post(self, request):
        serializer = InformationProfileSerailizer(
            data=request.data, instance=request.user.information
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"update_profile_file": serializer.data}, status=201)


class EmailUsernameOnly(APIView):
    def get(self, request):
        data = User.objects.get(id=request.user.id)
        serializer = UserSerailizerEmailUsername(data)
        return Response(serializer.data, status=201)
