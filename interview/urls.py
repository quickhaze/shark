from django.urls import path, include
from .views import *
from rest_framework import routers
from .api import *
router = routers.DefaultRouter()
 
router.register(r'jobs', JobsViewSet, basename='Job')
router.register(r'resume', ApplicationViewSet, basename='application')
router.register(r'question', QuestionViewSet, basename='question')
router.register(r'interviewupdate', InterviewUpdateViewSet, basename='interviewupdate')
router.register(r'candidateviewSet', CandidateViewSet, basename='candidateviewSet')
router.register(r'qualification', QualificationViewSet, basename='qualificationupdateviewSet')

 
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path("questions/", QuestionIndexView.as_view(), name="question-index"),

]
