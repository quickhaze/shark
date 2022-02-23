from django.urls import path, include
from .views import *
from rest_framework import routers

router = routers.DefaultRouter()
router.register("developer", Developer_add, basename="developer_add")
router.register("role", Role_add, basename="developer_add")


urlpatterns = [
    path("allrole/", RoleList.as_view()),
    path("roleGet/<int:pk>/", RoleGet.as_view()),
    path("alldeveloper/", DeveloperList.as_view()),
    path("developerGet/<int:pk>", DeveloperGet.as_view()),
    path("", include(router.urls)),
]
