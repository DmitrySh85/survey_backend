from rest_framework.generics import (
    ListAPIView,
    CreateAPIView
)

from .serializers import (
    QuestionSerializer,
    DailySurveyCounterSerializer,
    IncreaseDailySurveyCounterSerializer
)
from rest_framework.permissions import IsAuthenticated
from .services import (
    get_questions_filters,
    get_filtered_questions
)
from .models import DailySurveyCounter
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import datetime


class QuestionListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer

    def get_queryset(self):
        filters = get_questions_filters(self.request)
        queryset = get_filtered_questions(filters)
        return queryset


class CreateDailySurveyCounter(CreateAPIView):
    queryset = DailySurveyCounter.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = DailySurveyCounterSerializer


class IncreaseDayliSurveyCounter(APIView):
    permission_classes = [IsAuthenticated]

    def get_serializer_class(self):
        return IncreaseDailySurveyCounterSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer_class()(data=request.data)
        if serializer.is_valid():
            data = serializer.validated_data
            employee_id = data.get("employee")
            attempts_counter = DailySurveyCounter.objects.get(
                employee__id=employee_id,
                date=datetime.today()
            )
            attempts_count = attempts_counter.attempts + 1
            attempts_counter.attempts = attempts_count
            attempts_counter.save()
            return Response({"ok": True})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)