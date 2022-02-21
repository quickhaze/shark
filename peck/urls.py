from unicodedata import name
from django.urls import path
from .views import *
from . import views

urlpatterns = [
    # path("rolelist/", RoleList.as_view()),
    # path("rolelist/<int:pk>/", RoleGet.as_view()),
    # path("developerlist/", DeveloperList.as_view()),
    # path("developerlist/<int:pk>", DeveloperGet.as_view()),
    path("rolelist/", views.RoleList, name="RoleList"),
    path("rolelist/<int:id>/", views.RoleGet, name="RoleGet"),
    path("developerlist/", views.DeveloperList, name="DeveloperList"),
    path("developerlist/<int:id>", views.DeveloperGet, name="DeveloperGet"),
]
