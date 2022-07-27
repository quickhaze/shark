from django.db import models

# Create your models here.


class InitModel(models.Model):
    """ """

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return f"{self.created_at}"


class Technology(models.Model):
    technology = models.CharField(max_length=50)

    def __str__(self):
        return self.technology
