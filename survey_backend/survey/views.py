from rest_framework.generics import ListAPIView
from .serializers import QuestionSerializer
from rest_framework.permissions import IsAuthenticated
from .services import (
    get_questions_filters,
    get_filtered_questions
)


class QuestionListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = QuestionSerializer

    def get_queryset(self):
        filters = get_questions_filters(self.request)
        queryset = get_filtered_questions(filters)
        return queryset
