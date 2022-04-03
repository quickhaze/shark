from django.db import models
from django.urls import reverse
from root.models import InitModel
from django.contrib.auth.models import User
# Create your models here.

REPO_TYPE = (
    ("github", "github"),
    ("gitlab", "gitlab"),
    ("bitbucket", "bitbucket"),
    ("zip", "zip"),
)
AUTH_TYPE = (
    ("google", "google"),
    ("username_password", "username_password"),
    ("other", "other"),
)


class Project(InitModel):
    name = models.CharField(max_length=50)
    about = models.TextField(
        null=True, blank=True, help_text="Short description about the project"
    )
    logo = models.FileField(blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.name}"


class BaseProject(InitModel):
    project = models.ForeignKey(
        Project, on_delete=models.SET_NULL, blank=True, null=True
    )
    username = models.CharField(max_length=50, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    password = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self) -> str:
        return f"{self.project}"

    class Meta:
        abstract = True


class Repository(BaseProject):
    repo_type = models.CharField(
        choices=REPO_TYPE, max_length=50, blank=True, null=True
    )
    auth_type = models.CharField(
        choices=AUTH_TYPE, max_length=50, blank=True, null=True
    )
    url = models.URLField(blank=True, null=True)


class Category(InitModel):
    name = models.CharField(max_length=50)
    about = models.TextField(
        null=True, blank=True, help_text="Short description about the category"
    )

    def __str__(self) -> str:
        return f"{self.name}"


class Credentials(BaseProject):
    credential_type = models.CharField(
        max_length=50,
        blank=True,
        null=True,
        help_text="Describe what this credentials are about",
    )
    url = models.URLField(
        blank=True, null=True, help_text="URL for which credentials are being added"
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        help_text="Category such as staging server aws or jira",
    )
    file = models.FileField(upload_to="auth_files", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.credential_type}"

 
class ProjectDocument(BaseProject):
    name = models.CharField(max_length=50)
    url = models.URLField(blank=True, null=True)
    file = models.FileField(upload_to="auth_files", null=True, blank=True)

    def __str__(self) -> str:
        return f"{self.name}- {self.project}"


class Extra(InitModel):
    extra = models.JSONField(default=dict)
    project = models.ForeignKey(
        Project, on_delete=models.SET_NULL, blank=True, null=True
    )

    def __str__(self) -> str:
        return f"{self.project}"


class AssignedProject(InitModel):
    user = models.OneToOneField(User, on_delete=models.SET_NULL, null=True, blank=True, related_name="projects")
    projects = models.ManyToManyField(Project, blank=True)

    def __str__(self) -> str:
        return f"{self.user}"
