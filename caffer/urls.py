from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register("user", UserViewsets, basename="user")
router.register(
    "projectdeveloper", ProjectDeveloperViewset, basename="projectdeveloper"
)
router.register("roleinproject", RoleInProjectViewset, basename="roleinproject")
router.register("project", ProjectViewset, basename="project")


urlpatterns = [
    path("alluser/", AllUser.as_view()),
    path("userdetails/<str:username>/", UserGet.as_view()),
    path("allproject/", AllProject.as_view()),
    path("projectdetails/<str:project_name>/", ProjectGet.as_view()),
    path("", include(router.urls)),
]
