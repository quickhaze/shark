# import serializer from rest_framework
from dataclasses import field
from platform import java_ver
from rest_framework import serializers
 
# import model from models.py
from .models import *
 
# Create a model serializer
class JobsSerializer(serializers.ModelSerializer):
    # specify model and fields 
    class Meta:
        model = Job
        fields = ('job_name', 'job_description','number_of_openings', 'experience_requride', 'responsibilities', 'requirement', 'perks_and_benefits')

# Create a model serializer
class CandidateSerializer(serializers.ModelSerializer):
    # specify model and fields 
    class Meta:
        model = Candidate
        fields = '__all__'

# Create a model serializer
class ApplicationSerializer(serializers.ModelSerializer):
    # specify model and fields 
    class Meta:
        model = Application
        fields = '__all__'


# Create a model serializer
class QuestionSerializer(serializers.ModelSerializer):
    # specify model and fields 
    class Meta:
        model = Question
        fields = '__all__'


# Create a model serializer
class InterviewUpdateSerializer(serializers.ModelSerializer):
    # specify model and fields 
    class Meta:
        model = InterviewUpdate
        fields = '__all__'

# Create a model serializer
class QualificationSerializer(serializers.ModelSerializer):
    # specify model and fields 
    class Meta:
        model = Qualification
        fields = '__all__'
