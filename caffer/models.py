from statistics import mode
from django.db import models
from django.utils.translation import ugettext as _
from peck.models import Developer
from root.models import InitModel


# Create your models here.
class Project(InitModel):
    """
    """
    name = models.CharField(max_length=200, help_text=_("The name of the project"))
    cracker = models.CharField(
        max_length=200,
        help_text=_("The name of the developer who cracked the interview"),
    )
    developer = models.ManyToManyField(
        Developer,
        through = "caffer.ProjectDeveloper",
        verbose_name=_("developers"),
        help_text=_(
            "The name of the developers contributed to the project on the project"
        ),
    )


class ProjectDeveloper(InitModel):
    project = models.ForeignKey("caffer.project", on_delete=models.PROTECT)
    developer = models.ForeignKey("peck.developer", on_delete=models.PROTECT)
    role_in_project = models.ManyToManyField("peck.roles", through="caffer.roleinproject")

    class Meta:
        ordering = ('created_at')

class RoleInProject(InitModel):
    project = models.ForeignKey(ProjectDeveloper, on_delete=models.PROTECT)
    developer = models.ForeignKey("peck.developer", on_delete=models.PROTECT)
    role = models.ManyToManyField("peck.roles")

    class Meta:
        ordering = ('created_at')