from rest_framework.serializers import ModelSerializer, Serializer, UUIDField
from .models import Question, DailySurveyCounter


class QuestionSerializer(ModelSerializer):
    class Meta:
        model = Question
        fields = "__all__"


class DailySurveyCounterSerializer(ModelSerializer):
    class Meta:
        model = DailySurveyCounter
        fields = "__all__"

    
class IncreaseDailySurveyCounterSerializer(Serializer):

    employee = UUIDField()