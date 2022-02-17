from statistics import mode
from django.db import models
from root.models import InitModel

# Create your models here.
from django.contrib.auth.models import User

ROLE = (
    ("sde1", "Software Developer I"),
    ("sde2", "Software Developer II"),
    ("sde3", "Software Developer III"),
    ("sde4", "Software Developer IV"),
    ("graphic_designer", "Graphic Designer"),
    ("qa", "Quality Analyst"),
    ("python_developer", "Python Developer"),
    ("django_developer", "Django Developer"),
    ("tl", "Team_leader"),
    ("project_manager", "Project Manager"),
  


)


class Role(models.Model):
    role = models.CharField(max_length=30, choices=ROLE, unique=True)

    def __str__(self) -> str:
        return f"{self.role}"


class Developer(InitModel):
    user = models.OneToOneField(User, on_delete=models.PROTECT)
    role = models.ManyToManyField(Role)

    def __str__(self) -> str:
        return f"{self.user}"
