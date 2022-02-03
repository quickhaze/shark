from django.urls import path, include
from root import views
from .views import *

app_name = "root"

urlpatterns = [
    path("administration", views.administration, name="administration"),
    path("", IndexView.as_view(), name="index"),
    path("home/", HomeView.as_view(), name="home-view"),
]
