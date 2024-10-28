from django.contrib import admin
from .models import Question


class QuestionAdmin(admin.ModelAdmin):

    list_display = ('text', 'description', 'valid_answer_number',)
    list_display_links = ('text',)


admin.site.register(Question, QuestionAdmin)



