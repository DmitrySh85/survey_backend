from django.db import models


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

