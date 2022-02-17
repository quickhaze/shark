from rest_framework import serializers
from .models import *

class RoleSerializers(serializers.ModelSerializer):
    class Meta:
        model=Role
        fields=['role']

class DeveloperSerializers(serializers.ModelSerializer):
    # role=RoleSerializers(read_only=True)
    # role=serializers.ReadOnlyField(source='role')
    class Meta:
        model=Developer
        fields=['user','role']

    def to_representation(self, instance):
        data=super().to_representation(instance)
        # import pdb;pdb.set_trace()
        new=[]
        for i in data['role']:
            abc= Role.objects.get(pk=i).role
            new.append(abc)
        data['user']=User.objects.get(pk=instance.user_id).username
        data['role']=new
        return data

