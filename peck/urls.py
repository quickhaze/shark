from unicodedata import name
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    # path("rolelist/", RoleList.as_view()),
    # path("rolelist/<int:pk>/", RoleGet.as_view()),
    # path("developerlist/", DeveloperList.as_view()),
    # path("developerlist/<int:pk>", DeveloperGet.as_view()),
    path("rolelist/", views.roleList, name="RoleList"),
    path("rolelist/<int:id>/", views.roleGet, name="RoleGet"),
    path("developerlist/", views.developerList, name="DeveloperList"),
    path("developerlist/<int:id>", views.developerGet, name="DeveloperGet"),
]
