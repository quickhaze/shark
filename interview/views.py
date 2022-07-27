import json
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import JobsSerializer
from .models import Job
from .questions import question_list
import random
# from django.contrib.auth.decorators import login_required
from django.views import View


class JobsViewSet(viewsets.ModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobsSerializer
# Create your views here.


# @login_required
class QuestionIndexView(View):

    def get(self, request, *args, **kwargs):
        ctx = {"questions": question_list}
        return render(request, 'questions-index.html', ctx)

    
    def post(self, request, *args, **kwargs):
        ctx = {"questions": question_list}
        return render(request, 'questions-index.html', ctx)
