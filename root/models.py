from django.db import models

# Create your models here.

class InitModel(models.Model):
    '''
    '''
    created_at = models.DateTimeField(auto_created=True)
    updated_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        abstract = True

    def __str__(self) -> str:
        return self.created_at
