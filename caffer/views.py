from django.http import HttpResponse
from .models import *
from .serializer import *
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404


class ProjectViewset(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer


class ProjectDeveloperViewset(viewsets.ModelViewSet):
    queryset = ProjectDeveloper.objects.all()
    serializer_class = ProjectDeveloperSerializer


class RoleInProjectViewset(viewsets.ModelViewSet):
    queryset = RoleInProject.objects.all()
    serializer_class = RoleInProjectSerializer


class UserViewsets(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserRegisterSerializers


class AllUser(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserDetails


class UserGet(APIView):
    def get_object(self, username):
        try:
            return User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, username):
        import pdb

        pdb.set_trace()
        data = self.get_object(username)
        serializer = UserDetails(data)
        return Response(serializer.data)


class AllProject(ListAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectDetails


class ProjectGet(APIView):
    def get_object(self, project_name):
        try:
            return Project.objects.get(name__iexact=project_name)
        except User.DoesNotExist:
            raise Http404

    def get(self, request, project_name):
        data = self.get_object(project_name)
        serializer = ProjectDetails(data)
        return Response(serializer.data)
