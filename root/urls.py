from django.urls import path, include
from root import views
from .views import *
from django.contrib.auth import views as auth_views

app_name = "root"

urlpatterns = [
    # path("administration", views.administration, name="administration"),
    path("", UserListView.as_view(), name="index"),
    path("page/", PageView.as_view(), name="page"),
    path(
        "login/",
        auth_views.LoginView.as_view(
            template_name="login.html", redirect_field_name="/server/"
        ),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    # path("home/", HomeView.as_view(), name="home-view"),
]
