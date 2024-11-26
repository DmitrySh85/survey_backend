from django.urls import path
from .views import (
    QuestionListAPIView,
    CreateDailySurveyCounter,
    IncreaseDayliSurveyCounter
)


urlpatterns = [
    path("questions/", QuestionListAPIView.as_view(), name="questions"),
    path("attempts/", CreateDailySurveyCounter.as_view(), name="create_counter"),
    path("attempts/increase/", IncreaseDayliSurveyCounter.as_view(), name="increase_counter"),
]