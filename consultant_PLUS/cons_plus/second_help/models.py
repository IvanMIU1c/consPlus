from django.db import models
from django.core.files.storage import FileSystemStorage



fs = FileSystemStorage(location="./media/materials")


class Solution(models.Model):
    solution_text = models.TextField(verbose_name='Краткое описание решения')
    document_template = models.FileField(storage=fs, verbose_name='Шаблон документа')


class Question(models.Model):
    PRODUCT = 'product'
    REPAIR = 'repair'
    TYPE_CHOICES = [(PRODUCT, 'Product'),
                    (REPAIR, 'Repair')]

    problem_type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name='Тип проблемы')
    question_wording = models.CharField(max_length=512, verbose_name='Формулировка вопроса')
