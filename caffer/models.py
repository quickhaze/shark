from statistics import mode
from django.db import models
from django.utils.translation import gettext_lazy as _
from peck.models import Developer
from root.models import InitModel


# Create your models here.
class Project(InitModel):
    """ """

    name = models.CharField(max_length=200, help_text=_("The name of the project"))
    cracker = models.ForeignKey(
        Developer,
        max_length=200,
        help_text=_("The name of the developer who cracked the interview"),
        on_delete=models.PROTECT,
        related_name="project_cracker",
    )
    developer = models.ManyToManyField(
        to=Developer,
        through="caffer.ProjectDeveloper",
        verbose_name=_("developers"),
        help_text=_(
            "The name of the developers contributed to the project on the project"
        ),
    )

    def __str__(self) -> str:
        return f"{self.name}"


class ProjectDeveloper(InitModel):
    """ """

    project = models.ForeignKey("caffer.project", on_delete=models.PROTECT)
    developer = models.ForeignKey("peck.developer", on_delete=models.PROTECT)
    role_in_project = models.ManyToManyField(
        to="peck.role", through="caffer.roleinproject"
    )

    class Meta:
        ordering = ("created_at",)


class RoleInProject(InitModel):
    """ """

    projectdeveloper = models.ForeignKey(ProjectDeveloper, on_delete=models.PROTECT)
    role = models.ForeignKey(to="peck.role", on_delete=models.PROTECT)

    class Meta:
        ordering = ("created_at",)
