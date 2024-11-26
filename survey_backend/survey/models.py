from django.db import models
from employees.models import Employee


class Question(models.Model):
    text = models.TextField(max_length=1000)
    first_answer = models.TextField(max_length=300)
    second_answer = models.TextField(max_length=300, null=True, blank=True)
    third_answer = models.TextField(max_length=300, null=True, blank=True)
    fourth_answer = models.TextField(max_length=300, null=True, blank=True)
    valid_answer_number = models.IntegerField()
    description = models.TextField(max_length=300, null=True, blank=True)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class DailySurveyCounter(models.Model):
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE, related_name="attempts")
    attempts = models.IntegerField(default=1)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"Попытки для {self.employee} за {self.date}"

    class Meta:
        unique_together = ("employee", "date")
        verbose_name = "Счетчик заданий"
        verbose_name_plural = "Счетчики заданий"

