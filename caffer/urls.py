from django.urls import path
from .views import *

urlpatterns = [
    path("prolist/", ProjectList1.as_view()),
    path("projectdeveloperlist/", ProjectDeveloperList.as_view()),
    path("projectdeveloperlist/<int:pk>/", ProjectDeveloperGet.as_view()),
    path("roleinprojectlist/", RoleInProjectList.as_view()),
    path("roleinprojectlist/<int:pk>/", RoleInProjectGet.as_view()),
    path("prolist/<int:pk>/", ProjectGet1.as_view()),
]
