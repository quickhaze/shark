import csv

from django.contrib.auth.mixins import PermissionRequiredMixin
from django.http import HttpResponse, HttpResponseNotFound, JsonResponse
from django.shortcuts import redirect, render
from django.urls import reverse
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.views import APIView
from root.models import Technology

from info.models import LookUp
from info.templatetags.present import last_day_of_month

from .models import Attendance, UserInformation
from .serializer import *


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


from datetime import date

from django.views import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView

from .forms import DocumetsForm

# from django.views.generic
from .models import Documents

Any = object
from django.contrib.auth.mixins import LoginRequiredMixin


class Profile(LoginRequiredMixin, DetailView):
    model = User
    template_name = "user-profile.html"

    def get_context_data(self, **kwargs: Any):
        ctx = super().get_context_data(**kwargs)
        ctx['month'] = int(self.request.GET.get('month', date.today().month))
        ctx['month_name'] = date.today().replace(month=ctx['month']).strftime("%B")
        return ctx


class DocUpload(LoginRequiredMixin, View):
    def post(self, request, *args, **kwargs):
        form =  (request.POST, request.FILES)
        if form.is_valid():
            Documents.objects.create(
                user_info=request.user.userinformation if not request.user.is_superuser else User.objects.get(pk=int(request.GET.get('user_id'))),
                **form.cleaned_data
            )
        return redirect(reverse("root:index"))


class AttendanceView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        today = date.today()
        instance = Attendance.objects.filter(
            user=request.user,
            created_at__year=today.year,
            created_at__month=today.month,
            created_at__day=today.day,
        ).first()
        if not instance:
            instance = Attendance.objects.create(user=request.user)
        instance.save()
        return JsonResponse({"success": True}, status=200)


# class DownloadAtendanceView(LoginRequiredMixin,PermissionRequiredMixin, View):
class DownloadAtendanceView(View):
    # permission_required = 'polls.add_choice'

    def get(self, request):
        num = last_day_of_month() + 1
        data = [["Dates"], ["Days"]]
        data.append(["" for x in range(1, num + 2)])
        data.append(["Names"])
        for x in range(1, last_day_of_month() + 1):
            data[0].append(x)
            data[2].append("")
            data[1].append(date.today().replace(day=x).strftime("%a"))
        data[1].append("Total")
        for user in User.objects.all():
            try:
                data.append(
                    [user.first_name if user.first_name else user.username]
                    + [*user.look.attendance.values()]
                    + [sum([1 if y is True else 0 for y in user.look.attendance.values()])]
                )
            except LookUp.DoesNotExist as e:
                data.append(
                    [user.first_name if user.first_name else user.username]
                    + ["-" for _ in range(1, num)]
                )

        with open(f"Attendance-{date.today()}.csv", "w+", newline="") as f:
            writer = csv.writer(f)
            writer.writerows(data)
        try:
            with open(f"Attendance-{date.today()}.csv", "r") as f:
                file_data = f.read()

                # sending response
                response = HttpResponse(
                    file_data, content_type="application/vnd.ms-excel"
                )
                response[
                    "Content-Disposition"
                ] = f'attachment; filename="Attendance-{date.today()}.csv"'

        except IOError:
            # handle file not exist case here
            response = HttpResponseNotFound("<h1>File not exist</h1>")

        return response
