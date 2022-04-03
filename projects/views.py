import re
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Category, Credentials, Project, Repository, ProjectDocument
from .forms import RepositoryForm, CredentialsFrom, ProjectDocumentFrom
from django.views.generic.edit import CreateView

BASE_URL = "127.0.0.1:8000/root/"


class ProjectsView(LoginRequiredMixin, View):
    def get(self, request, *args, **kwargs):
        if pk := kwargs.get("pk"):
            ctx = {
                "project": Project.objects.get(pk=pk),
                "repository_from": RepositoryForm(),
                "credentials_form": CredentialsFrom(),
                "project_doc_from": ProjectDocumentFrom(),
            }
            return render(request, "project-detail.html", ctx)
        projects = Project.objects.all()
        if not request.user.is_superuser:
            projects = request.user.projects.projects.all()
        ctx = {"projects": projects}
        return render(request, "projects.html", ctx)


class AddRepoView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwrags):
        form = RepositoryForm(
            request.POST,
        )
        if form.is_valid():
            project = Project.objects.get(pk=kwrags.get("pk"))
            cleaned_data = form.cleaned_data
            cleaned_data["project"] = project
            Repository.objects.create(**cleaned_data)
        return redirect(reverse("projects:list"))


class AddCredentialView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwrags):
        form = CredentialsFrom(request.POST, request.FILES)
        if form.is_valid():
            project = Project.objects.get(pk=kwrags.get("pk"))
            cleaned_data = form.cleaned_data
            cleaned_data["project"] = project
            Credentials.objects.create(**cleaned_data)
        return redirect(reverse("projects:list"))


class AddDocView(LoginRequiredMixin, View):
    def post(self, request, *args, **kwrags):
        form = ProjectDocumentFrom(request.POST, request.FILES)
        if form.is_valid():
            project = Project.objects.get(pk=kwrags.get("pk"))
            cleaned_data = form.cleaned_data
            cleaned_data["project"] = project
            ProjectDocument.objects.create(**cleaned_data)
        return redirect(reverse("projects:list"))


class CategoryAddView(LoginRequiredMixin, CreateView):
    model = Category
    fields = "__all__"

    def get_success_url(self) -> str:
        return reverse("projects:list")


AddDocView
