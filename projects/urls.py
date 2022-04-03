from django.urls import path, include
from root import views
from .views import *

app_name = "projects"

urlpatterns = [
    path("", ProjectsView.as_view(), name="list"),
    path("<int:pk>/", ProjectsView.as_view(), name="detail"),
    path("<int:pk>/add-repo/", AddRepoView.as_view(), name="add-repo"),
    path("<int:pk>/add-cred/", AddCredentialView.as_view(), name="add-cred"),
    path("<int:pk>/add-doc/", AddDocView.as_view(), name="add-doc"),
    path("category", CategoryAddView.as_view(), name="category"),
]
