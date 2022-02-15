from django.db import models
from django.contrib.auth.models import User
from datetime import datetime
# Create your models here.


class Information(models.Model):
    TYPE=(('student','STUDENT'),('employe','EMPLOYE'))
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    git_url=models.URLField()
    git_username=models.CharField(max_length=50)
    user_adress=models.TextField()
    phone_number=models.CharField(max_length=12)
    qualification=models.CharField(max_length=20)
    technology=models.CharField(max_length=50)
    project_description=models.TextField()
    team_leader=models.CharField(max_length=50)
    team_memeber_names=models.TextField()
    joining_date=models.DateField(default=datetime.now())
    separation_date=models.DateField(null=True,blank=True)
    company_name=models.CharField(max_length=100)
    experiance=models.IntegerField()
    user_type=models.CharField(max_length=20,choices=TYPE)
    user_role=models.CharField(max_length=50)

    
    class Meta:
        ordering=['-id']

    def __str__(self):
        return self.git_username+'-'+self.user.username
