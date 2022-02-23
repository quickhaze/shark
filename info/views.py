from functools import partial
from turtle import pd
from django.http import Http404
from django.shortcuts import render
from .models import Information
from .serializer import *

# Create your views here.
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from root.models import Technology


# InfoAPI():
#   post():
#     xl  =request.user.information
#     xl.technology = request.data['technology']
#     xl.save()


class InfoCreate(APIView):

    # def get(self,request):
    #     import pdb;pdb.set_trace()
    #     print(request.user.information)
    #     data=User.objects.all()
    #     serializer=UserSerailizer(data,many=True)
    #     return Response(serializer.data)

    def post(self, request):

        xl = request.user.information
        # import pdb;pdb.set_trace()
        newdict = {
            "user": xl.user_id,
            "profile": xl.profile,
            "technology": xl.technology,
            "experiance": xl.experiance,
            "qualification": xl.qualification,
            "phone_number": xl.phone_number,
            "joining_date": xl.joining_date,
            "separation_date": xl.separation_date,
            "address": xl.address,
        }
        
        if request.data.get("technology"):
            all = request.data["technology"].split(",")
            for i in all:

                xl.technology.add(Technology.objects.get(technology__iexact=i))
        # elif not request.data.get('technology'):
        #     xl.technology.add(Technology.objects.none())

        xl.phone_number = request.data.get("phone_number", newdict["phone_number"])
        xl.profile = request.data.get("profile", newdict["profile"])
        xl.experiance = request.data.get("experiance", newdict["experiance"])
        xl.qualification = request.data.get("qualification", newdict["qualification"])
        xl.joining_date = request.data.get("joining_date", newdict["joining_date"])
        xl.separation_date = request.data.get(
            "separation_date", newdict["separation_date"]
        )
        xl.address = request.data.get("address", newdict["address"])
        xl.save()

        serializer = InformationSerailizer(data=newdict, partial=True)
        if serializer.is_valid():
            serializer.save()
            import pdb

            pdb.set_trace()

            return Response(serializer, status=201)
        return Response(serializer.errors, status=404)
