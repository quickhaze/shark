import json
from django.shortcuts import render
from django.views import View
# Create your views here.
from .questions import question_list
import random

@login_required
class QuestionIndexView(View):

    def get(self, request, *args, **kwargs):
        ctx = {"questions": question_list}
        return render(request, 'questions-index.html', ctx)

    
    def post(self, request, *args, **kwargs):
        import pdb; pdb.set_trace()
        return False