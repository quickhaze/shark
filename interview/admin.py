from django.contrib import admin
from .models import *

admin.site.register(Interviewer)
admin.site.register( Candidate)
admin.site.register( Job)
admin.site.register( Application)
admin.site.register( Qualification)
admin.site.register( InterviewUpdate)
admin.site.register( Question)
admin.site.register( Assesment)

