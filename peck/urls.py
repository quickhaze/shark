from django.urls import path, include
from .views import *
from rest_framework import routers
from peck import views

router = routers.DefaultRouter()
router.register("developer", Developer_add, basename="developer_add")
router.register("role", Role_add, basename="Role_add")


urlpatterns = [
    path("allrole/", RoleAllList.as_view()),
    path("roleGet/<int:pk>/", RoleGetById.as_view()),
    path("alldeveloper/", DeveloperAllList.as_view()),
    path("developerGet/<int:pk>", DeveloperGetById.as_view()),
    path("", include(router.urls)),
    path("rolelist/", views.RoleList, name="RoleList"),
    path("rolelist/<int:id>/", views.RoleGet, name="RoleGet"),
    path("developerlist/", views.DeveloperList, name="DeveloperList"),
    path("developerlist/<int:id>", views.DeveloperGet, name="DeveloperGet"),
]
