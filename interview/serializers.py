# import serializer from rest_framework
from platform import java_ver
from rest_framework import serializers
 
# import model from models.py
from .models import Job
 
# Create a model serializer
class JobsSerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = Job
        fields = ('job_name', 'job_description','number_of_openings', 'experience_requride', 'responsibilities', 'requirement', 'perks_and_benefits')