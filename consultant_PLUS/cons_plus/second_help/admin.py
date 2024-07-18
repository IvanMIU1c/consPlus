from django.contrib import admin
from .models import *


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('problem_type', 'question_wording', 'id')


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    list_display = ('question', 'text', 'next_question', 'id', 'solution')


@admin.register(Solution)
class SolutionAdmin(admin.ModelAdmin):
    list_display = ('solution_text', 'document_template', 'article')


@admin.register(Articles)
class ArticlesAdmin(admin.ModelAdmin):
    list_display = ('name', 'web_url', 'document')


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('name', )


@admin.register(DocumentTemplates)
class DocumentTemplatesAdmin(admin.ModelAdmin):
    list_display = ('name', 'document')

