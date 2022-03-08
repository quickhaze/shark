from email.policy import default
from pyexpat import model

from django.forms import Field
from rest_framework import serializers
from .models import *
from peck.models import *
from peck.models import *
from datetime import date


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ["id", "name", "cracker"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["cracker"] = Developer.objects.get(pk=instance.cracker_id).user.username
        return data


class ProjectDeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDeveloper
        fields = ["project", "developer"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["project"] = Project.objects.get(pk=instance.project_id).name
        data["developer"] = Developer.objects.get(
            pk=instance.developer_id
        ).user.username
        return data


class RoleInProjectSerializer(serializers.ModelSerializer):
    start_date = serializers.DateField(required=False, default=date.today)
    end_date = serializers.DateField(required=False, allow_null=True)

    class Meta:
        model = RoleInProject
        fields = ["id", "projectdeveloper", "role", "start_date", "end_date"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["projectdeveloper"] = ProjectDeveloper.objects.get(
            pk=instance.projectdeveloper_id
        ).project.cracker.user.username
        data["role"] = Role.objects.get(pk=instance.role_id).role
        return data


class UserRegisterSerializers(serializers.ModelSerializer):
    password1 = serializers.CharField(
        style={"input_type": "password"}, write_only=True, min_length=8
    )
    password2 = serializers.CharField(
        style={"input_type": "password"}, write_only=True, min_length=8
    )

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            "username",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]

    def validate(self, attrs):
        data = super().validate(attrs)
        if data["password1"] != data["password2"]:
            raise serializers.ValidationError("password not match")
        return data

    def create(self, validated_data):

        us = User.objects.create(
            email=self.validated_data["email"],
            username=self.validated_data["username"],
            first_name=self.validated_data["first_name"],
            last_name=self.validated_data["last_name"],
        )
        us.set_password(self.validated_data["password1"])
        us.save()
        return us


# class ProjectSeializer1(serializers.ModelSerializer):
#     developer = serializers.SerializerMethodField()

#     class Meta:
#         model = Project
#         fields = ["id", "name", "cracker", "developer"]

#     def to_representation(self, instance):
#         data = super().to_representation(instance)
#         data["cracker"] = Developer.objects.get(pk=instance.cracker_id).user.username
#         return data

#     def get_developer(self, obj):
#         abc = []
#         data = RoleInProject.objects.filter(projectdeveloper__project__name=obj.name)
#         help = {}
#         h = {}
#         l = []
#         for new in data:

#             h = {
#                 "developer_name": new.projectdeveloper.developer.user.username,
#                 "role": new.role.role,
#                 "start_date": new.start_date,
#                 "end_date": new.end_date,
#             }
#             abc.append(h)

#         for new in data:
#             kill_data = []
#             for j in range(len(abc)):
#                 if (
#                     abc[j]["developer_name"]
#                     == new.projectdeveloper.developer.user.username
#                 ):
#                     kill_data.append(abc[j])

#             help = {
#                 "developer_name": new.projectdeveloper.developer.user.username,
#                 "role": kill_data,
#             }

#             l.append(help)

#         final = []
#         final2 = []
#         tt = 0
#         for i in l:
#             if i["developer_name"] not in final:
#                 final2.append(i)
#                 final.append(i["developer_name"])
#             tt = tt + 1

#         for i in final2:

#             for j in range(len(i["role"])):
#                 del i["role"][j]["developer_name"]

#         return final2


class RoleInProjectTestSerializers(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = RoleInProject
        fields = ["role", "start_date", "end_date"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        print("__", data)

        data["start_date"] = RoleInProject.objects.get(id=instance.id).start_date
        data["end_date"] = RoleInProject.objects.get(id=instance.id).end_date
        return data

    def get_role(self, obj):
        a = Role.objects.get(id=obj.role_id)
        return a.role


class Project_Test(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ["name", "roles"]

    def get_roles(self, obj):
        data = ProjectDeveloper.objects.filter(project=obj.id)
        user = self.context["username"]
        for t in data:
            # a=ProjectDeveloper.objects.get(developer__user__id=t.developer_id)
            # for j in t.role_in_project.all():
            aa = RoleInProject.objects.filter(
                projectdeveloper__project__id=t.project_id,
                projectdeveloper__developer__user__username=user,
            )
            # import pdb;pdb.set_trace()
            # for i in range(len(aa)):
            # ak=RoleInProject.objects.filter(projectdeveloper__project__id=t.project_id,projectdeveloper__developer__user__id=t.developer_id)
            # print(ak)
            # ak=RoleInProject.objects.filter(projectdeveloper__project__id=t.project_id,projectdeveloper__developer__id=a.id,role__id=j.id)
            # ProjectDeveloper.objects.get(developer__user__id=t.id)--test
            # ak=RoleInProject.objects.filter(projectdeveloper__project__id=t.project_id,projectdeveloper__developer__id=t.developer_id)
            # print(ak)
            new = RoleInProjectTestSerializers(aa, many=True).data
            # new=RoleSerializers(t.role_in_project.all(),many=True).data
            return new


class UserDetails(serializers.ModelSerializer):
    project_details = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ["username", "email", "project_details"]

    def get_project_details(self, obj):
        data = Project.objects.filter(developer__user_id=obj.id)
        serializer = Project_Test(
            data, context={"username": obj.username}, many=True
        ).data
        return serializer


class RoleInProjectTestSerializeragain(serializers.ModelSerializer):
    role = serializers.SerializerMethodField()

    class Meta:
        model = RoleInProject
        fields = ["role", "start_date", "end_date"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["start_date"] = RoleInProject.objects.get(id=instance.id).start_date
        data["end_date"] = RoleInProject.objects.get(id=instance.id).end_date
        return data

    def get_role(self, obj):
        a = Role.objects.get(id=obj.role_id)
        return a.role


class ProjectDeveloperTestSerializer(serializers.ModelSerializer):
    roles = serializers.SerializerMethodField()

    class Meta:
        model = ProjectDeveloper
        fields = ["developer", "roles"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["developer"] = ProjectDeveloper.objects.get(
            id=instance.id
        ).developer.user.username
        return data

    def get_roles(self, obj):
        new = RoleInProject.objects.filter(projectdeveloper_id=obj.id)
        return RoleInProjectTestSerializeragain(new, many=True).data


class ProjectDetails(serializers.ModelSerializer):
    developers = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ["id", "name", "cracker", "developers"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["cracker"] = Developer.objects.get(id=instance.cracker_id).user.username
        return data

    def get_developers(self, obj):
        new = ProjectDeveloper.objects.filter(project__id=obj.id)
        return ProjectDeveloperTestSerializer(new, many=True).data
