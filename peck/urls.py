from django.urls import path
from .views import *

urlpatterns = [
    path("rolelist/", RoleList.as_view()),
    path("rolelist/<int:pk>/", RoleGet.as_view()),
    path("developerlist/", DeveloperList.as_view()),
    path("developerlist/<int:pk>", DeveloperGet.as_view()),
]
