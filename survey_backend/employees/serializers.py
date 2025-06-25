from datetime import datetime
from rest_framework.serializers import ModelSerializer
from .models import Employee
from survey.serializers import DailySurveyCounterSerializer


class EmployeeSerializer(ModelSerializer):

    attempts = DailySurveyCounterSerializer(many=True, read_only=True)

    class Meta:
        model = Employee
        fields = ["id", "tg_id", "name", "role", "created_at", "points", "is_blocked", "attempts"]

    def to_representation(self, instance):
        data = super().to_representation(instance)

        today = datetime.today()

        formatted_date = today.strftime('%Y-%m-%d')
        try:
            data["attempts"] = list(filter(lambda x: x.get("date") == formatted_date,data["attempts"]))[0]
        except Exception as e:
            data["attempts"] = None
        return data

