from django.urls import path, include
from .views import QuestionIndexView
urlpatterns = (
    [
        path("", QuestionIndexView.as_view(), name="question-index"),
    ]
)