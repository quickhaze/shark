from django.urls import path, include
from .views import *
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register("info_create", InfoCreate, basename="info_create")
app_name = "info"

urlpatterns = [
    path("info_create/", InfoCreate.as_view()),
    path("info_profile/", ProfileCreate.as_view()),
    path("email-user/", EmailUsernameOnly.as_view()),
    path("profile/<int:pk>/", Profile.as_view(), name="profile"),
    path("upload", DocUpload.as_view(), name="doc"),
    # path("", include(router.urls)),
]
