from django.urls import path
from .views import QuestionListAPIView


urlpatterns = [
    path("questions/", QuestionListAPIView.as_view(), name="questions"),
]