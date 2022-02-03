from django.urls import path, include
from root import views

app_name = "root"

urlpatterns = [
    path('administration',views.administration, name="administration")

   ]
