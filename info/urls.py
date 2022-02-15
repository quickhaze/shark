from django.urls import path,include
from .views import InfoCreate
from rest_framework import routers

router = routers.DefaultRouter()
router.register('info_create', InfoCreate,basename="info_create")

urlpatterns = [
    # path("info_create/", InfoCreate.as_view(), name="administration"),
    path('', include(router.urls)),
  
]
