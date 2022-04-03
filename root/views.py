from django.http import HttpResponse
from django.shortcuts import render
from django.views import View
from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.contrib.auth.mixins import LoginRequiredMixin

BASE_URL = "127.0.0.1:8000/root/"

class UserListView(LoginRequiredMixin, View):

    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        paginator = Paginator(users, 3)
        page_number = request.GET.get('page')
        page_obj = paginator.get_page(page_number)
        ctx ={
            "page_obj" : page_obj
        }
        return render(request, 'index.html', ctx)

class PageView(View):
    def get(self, request):
        return render(request, 'base.html', {})