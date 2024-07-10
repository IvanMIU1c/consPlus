from django.db import models
from django.core.files.storage import FileSystemStorage


fs = FileSystemStorage(location="./media/doc_templates")
fs_for_article = FileSystemStorage(location='./media/docs')


class Solution(models.Model):
    solution_text = models.TextField(verbose_name='Краткое описание решения')
    document_template = models.FileField(storage=fs, verbose_name='Шаблон документа')


class Question(models.Model):
    PRODUCT = 'Товар'
    REPAIR = 'Ремонт'
    TYPE_CHOICES = [(PRODUCT, 'Товар'),
                    (REPAIR, 'Ремонт')]
    last_question = models.BooleanField(default=True, verbose_name="Первый вопрос")
    problem_type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name='Тип проблемы')
    question_wording = models.CharField(max_length=512, verbose_name='Формулировка вопроса')
    solution = models.ForeignKey('Solution', on_delete=models.CASCADE, null=True, blank=True, related_name="solution", verbose_name="решение")


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='question')
    text = models.CharField(max_length=50)
    next_question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name="next_question")


class Articles(models.Model):
    web_url=models.CharField(max_length=1024, verbose_name="Внешняя ссылка")
    document = models.FileField(storage=fs_for_article, verbose_name="Файл документа")
