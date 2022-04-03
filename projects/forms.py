from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Repository, Project, Credentials, ProjectDocument


class RepositoryForm(forms.ModelForm):
    class Meta:
        model = Repository
        exclude = ("project",)


class CredentialsFrom(forms.ModelForm):
    class Meta:
        model = Credentials
        exclude = ("project",)


class ProjectDocumentFrom(forms.ModelForm):
    class Meta:
        model = ProjectDocument
        exclude = ("project",)
