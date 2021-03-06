from datetime import datetime
from django.db import models
from django.utils.translation import gettext_lazy as _
# Create your models here.
class Interviewer(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=12)
    technology = models.CharField(max_length=10)

    def __str__(self):
        return self.name
    
    def __repr__(self):
        return '<Interviewer %s>'% self.name

class Candidate(models.Model):

    class Gender(models.TextChoices):
        MALE = 'M', _('Male')
        FEMALE = 'F', _('Female')
        OTHER = 'O', _('Other')
    
    class JobURL(models.TextChoices):
        PYTHON = 'python', _('Python Developer')
        REACT = 'REACT', _('React Developer')
        HR = 'HR', _('Human Resource')
        BDE = 'BDE', _('Business Development Executive')

    class Source(models.TextChoices):
        LINKEDIN = 'IN', _('Linkedin')
        INDEED = 'INDEED', _('Indeed')
        APNA = 'APNA', _('Apna')
        NAUKARI = 'NAUKRI', _('Naukri')
        REFERENCE = 'REF', _('Reference')
        SOCIAL = 'SOCIAL', _('Social Media')
        CONSULTANCY = 'CONSULTANCY', _('Consultancy')
        OTHER = 'OTHER', _('Other')

    name = models.CharField(max_length=35)
    email = models.EmailField()
    phone1 = models.CharField(max_length=12)
    phone2 = models.CharField(max_length=12,null=True, blank=True)
    address = models.TextField(blank=True, null=True)

    gender = models.CharField(max_length=1, choices=Gender.choices)
    profile = models.CharField(max_length=6, choices=JobURL.choices, default='python')
    source = models.CharField(max_length=11, choices=Source.choices)
    # number_of_given_interview = models.IntegerField(default=1)

    def __str__(self):  
        return self.name
        
    def __repr__(self):
        return '<Candidate %s>'% self.name

class Job(models.Model):
    job_domain = models.CharField(max_length=15)
    job_openings = models.CharField(max_length=15)

    def __str__(self):
        return self.job_openings

    def __repr__(self):
        return '<Job %s>'% self.job_openings

class Application(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='applications')
    applying_job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='media')
    date= models.DateField(default=datetime.today)

    def __str__(self):
        return self.candidate
        
    def __repr__(self):
        return '<Application %s>'% self.candidate

class Qualification(models.Model):
    class Graduation(models.TextChoices):
        UG = 'UG', _('UG')
        PG = 'PG', _('PG')
        PHD = 'PHD', _('PHD')
        DIPLOMA = 'diploma', _('Diploma')

    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE)
    graduation_type = models.CharField(max_length=7, choices=Graduation.choices)
    degree = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    percentage =models.FloatField(max_length=4)
    institue = models.CharField(max_length=35)
    
    def __str__(self):
        return self.candidate

    def __repr__(self):
        return '<Qualification %s>'% self.candidate

class InterviewUpdate(models.Model):
    class InterviewRound(models.TextChoices):
        FIRST = 'first',_('First Round')
        SECOND = 'second',_('Second Round')
        FINAL = 'final', _('Final Round')

    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='interview_update')
    interviewer = models.ManyToManyField(Interviewer)
    interview_stage = models.CharField(max_length=6, choices=InterviewRound.choices)
    remark = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    follow_up = models.ForeignKey('self', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.application

    def __repr__(self):
        return '<InterviewUpdate %s>'% self.application