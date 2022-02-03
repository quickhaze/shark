from django.urls import path, include
from root import views
from .views import IndexView

app_name = "root"

urlpatterns = [
    path('administration',views.administration, name="administration"),
    path('', IndexView.as_view(), name="index"),
   ]


