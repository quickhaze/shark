from rest_framework import serializers
from .models import *
from peck.models import *


class ProjectDeveloperSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectDeveloper
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["project"] = Project.objects.get(pk=instance.project_id).name
        data["developer"] = Developer.objects.get(
            pk=instance.developer_id
        ).user.username
        new = []
        for i in data["role_in_project"]:
            a = Role.objects.get(pk=i).role
            new.append(a)
        data["role_in_project"] = new
        return data


class RoleInProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = RoleInProject
        fields = "__all__"

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["projectdeveloper"] = ProjectDeveloper.objects.get(
            pk=instance.projectdeveloper_id
        ).project.cracker.user.username
        data["role"] = Role.objects.get(pk=instance.role_id).role
        return data


class ProjectSeializer1(serializers.ModelSerializer):
    developer = serializers.SerializerMethodField()

    class Meta:
        model = Project
        fields = ["id", "name", "cracker", "developer"]

    def to_representation(self, instance):
        data = super().to_representation(instance)
        data["cracker"] = Developer.objects.get(pk=instance.cracker_id).user.username
        return data

    def get_developer(self, obj):
        abc = []
        data = RoleInProject.objects.filter(projectdeveloper__project__name=obj.name)
        help = {}
        h = {}
        l = []
        for new in data:

            h = {
                "developer_name": new.projectdeveloper.developer.user.username,
                "role": new.role.role,
                "start_date": new.start_date,
                "end_date": new.end_date,
            }
            abc.append(h)

        for new in data:
            kill_data = []
            for j in range(len(abc)):
                if (
                    abc[j]["developer_name"]
                    == new.projectdeveloper.developer.user.username
                ):
                    kill_data.append(abc[j])

            help = {
                "developer_name": new.projectdeveloper.developer.user.username,
                "role": kill_data,
            }

            l.append(help)
        # import pdb;pdb.set_trace()
        final = []
        final2 = []
        tt = 0
        for i in l:
            if i["developer_name"] not in final:
                final2.append(i)
                final.append(i["developer_name"])
            tt = tt + 1

        for i in final2:
            print(i)
            for j in range(len(i["role"])):
                del i["role"][j]["developer_name"]

        return final2
