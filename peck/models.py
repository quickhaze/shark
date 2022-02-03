from statistics import mode
from django.db import models
from root.models import InitModel

# Create your models here.
from django.contrib.auth.models import User

ROLE = (
    ("developer", "developer"),
    ("designer", "designer"),
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
