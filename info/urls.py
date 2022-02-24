from django.urls import path, include
from .views import *
from rest_framework import routers

# router = routers.DefaultRouter()
# router.register("info_create", InfoCreate, basename="info_create")

urlpatterns = [
    path("info_create/", InfoCreate.as_view()),
    path("info_profile/", ProfileCreate.as_view()),
    path("email-user/", EmailUsernameOnly.as_view()),
    # path("", include(router.urls)),
]
