from django.contrib import admin
from .models import *


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('first_question', 'problem_type', 'question_wording')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'next_question')