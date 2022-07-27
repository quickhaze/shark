from datetime import datetime
from statistics import mode
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.

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
    class Requirement(models.TextChoices):
        PYTHON = 'python', _('Python Developer')
        REACT = 'react', _('React Developer')
    job_name = models.CharField(max_length=105,null=True, blank=True)
    job_description = models.TextField(null=True, blank=True)
    number_of_openings = models.IntegerField(null=True, blank=True)
    experience_requride = models.IntegerField(validators=[MinValueValidator(0),MaxValueValidator(10 )], null=True, blank=True)
    responsibilities = models.TextField(null=True, blank=True)
    requirement = models.CharField(max_length=12, choices=Requirement.choices, default='python')
    perks_and_benefits = models.TextField(null=True, blank=True)


    # def __str__(self):
    #     return self.job_name

    # def __repr__(self):
    #     return '<Job %s>'% self.job_name

class Application(models.Model):
    candidate = models.ForeignKey(Candidate, on_delete=models.CASCADE, related_name='applications')
    applying_job = models.ForeignKey(Job, on_delete=models.CASCADE)
    resume = models.FileField(upload_to='media')
    date= models.DateField(default=datetime.today)

    def __str__(self):
        return self.candidate.name
        
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

class Question(models.Model):
    class QuestionLanguage(models.TextChoices):
        PYTHON = 'Python', _('Python')
        JAVASCRIPT = 'JavaScript', _('JavaScript')
    class QuestionLevel(models.TextChoices):
        HARD = 'Hard', _('Hard')
        MEDIUM = 'Medium', _('Medium')
        EASY = 'Easy', _('Easy')

    text = models.TextField()
    language = models.CharField(max_length=20, choices=QuestionLanguage.choices)
    level = models.CharField(max_length=20, choices=QuestionLevel.choices)
    answer = models.TextField()




class InterviewUpdate(models.Model):
    class InterviewRound(models.TextChoices):
        FIRST = 'first',_('First Round')
        SECOND = 'second',_('Second Round')
        FINAL = 'final', _('Final Round')

    application = models.ForeignKey(Application, on_delete=models.CASCADE, related_name='interview_update')
<<<<<<< HEAD
    interviewer = models.ManyToManyField(Interviewer)
    interview_stage = models.CharField(max_length=7, choices=InterviewRound.choices)
=======
    interviewer = models.ManyToManyField(User)
    interview_stage = models.CharField(max_length=6, choices=InterviewRound.choices)
>>>>>>> acd4f2b36252cdae75fff127ba2273500ea41b92
    remark = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)
    follow_up = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"{self.application}"

    def __repr__(self):
        return '<InterviewUpdate %s>'% self.application


class Assesment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.TextField()
    interview = models.ForeignKey(InterviewUpdate, on_delete=models.SET_NULL, null=True, blank=True)

