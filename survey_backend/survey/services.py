from django.db.models import QuerySet
from django.http import HttpRequest
from .models import Question
from .filters import QuestionsFilters


def get_questions_filters(request: HttpRequest) -> QuestionsFilters:
    length = request.query_params.get("length")
    filters = QuestionsFilters(length=int(length))
    return filters


def get_filtered_questions(filters: QuestionsFilters) -> QuerySet[Question]:
    queryset = Question.objects.all().order_by("?")[:filters.length]
    return queryset
