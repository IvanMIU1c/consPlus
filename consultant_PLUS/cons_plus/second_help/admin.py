from django.contrib import admin
from .models import *


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('problem_type', 'question_wording', 'solution', 'id')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'next_question', 'id')


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('solution_text', 'document_template', 'article')