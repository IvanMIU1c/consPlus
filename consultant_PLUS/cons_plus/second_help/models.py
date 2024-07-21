from django.core.validators import MaxValueValidator
from django.db import models
from django.core.files.storage import FileSystemStorage

fs = FileSystemStorage(location="./media/doc_templates")
fs_for_article = FileSystemStorage(location='./media/articles')


class Solution(models.Model):
    solution_text = models.TextField(verbose_name='Краткое описание решения')
    document_template = models.FileField(storage=fs, verbose_name='Шаблон документа', null=True, blank=True)
    article = models.ForeignKey('Articles', on_delete=models.CASCADE, null=True, blank=True, verbose_name='Статья')

    class Meta:
        verbose_name = "Решение"
        verbose_name_plural = "Решения"

    def __str__(self):
        return self.solution_text


class Question(models.Model):
    PRODUCT = 'Товар'
    REPAIR = 'Ремонт'
    TYPE_CHOICES = [(PRODUCT, 'Товар'), (REPAIR, 'Ремонт')]
    problem_type = models.CharField(max_length=20, choices=TYPE_CHOICES, verbose_name='Тип проблемы')
    question_wording = models.CharField(max_length=512, verbose_name='Формулировка вопроса')

    def __str__(self):
        return self.question_wording

    class Meta:
        verbose_name = "Вопрос"
        verbose_name_plural = "Вопросы"


class Answer(models.Model):
    question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name='question',
                                 verbose_name="Текущий вопрос")
    text = models.CharField(max_length=150)
    next_question = models.ForeignKey('Question', on_delete=models.CASCADE, related_name="next_question",
                                      verbose_name="Следующий вопрос", null=True, blank=True)
    solution = models.ForeignKey('Solution', on_delete=models.CASCADE, null=True, blank=True, related_name="solution",
                                 verbose_name="решение")

    class Meta:
        verbose_name = "Ответ"
        verbose_name_plural = "Ответы"


class Articles(models.Model):
    name = models.CharField(max_length=125, default="default_name")
    web_url = models.CharField(max_length=1024, verbose_name="Внешняя ссылка", null=True, blank=True)
    document = models.FileField(storage=fs_for_article, verbose_name="Файл документа", null=True, blank=True)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.name


class DocumentTemplates(models.Model):
    name = models.CharField(max_length=125, default='def_name')
    document = models.FileField(storage=fs, verbose_name="Шаблон документа", null=True, blank=True)
    tags = models.ManyToManyField('Tag')


class SolutionScore(models.Model):
    score = models.IntegerField(validators=[MaxValueValidator(5)], verbose_name='Оценка')
    average_score = models.IntegerField(verbose_name="Средняя оценка")
    solution = models.ForeignKey('Solution', on_delete=models.CASCADE, null=True, blank=True,
                                 related_name="scored_solution",
                                 verbose_name="решение")


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name
