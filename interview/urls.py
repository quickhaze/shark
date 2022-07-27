from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
 
router.register(r'jobs', JobsViewSet, basename='Job')
 
urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
    path("questions/", QuestionIndexView.as_view(), name="question-index"),

]
