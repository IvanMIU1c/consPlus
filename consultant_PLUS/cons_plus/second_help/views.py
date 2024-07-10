from django.shortcuts import render

from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Question, Answer


def home(request):
    context = {'catgories': Question.objects.all()}

    if request.GET.get('gfg'):
        return redirect(f"/quiz/?gfg={request.GET.get('gfg')}")

    return render(request, 'home.html', context)


def show_question(request, question_id):
    question = Question.objects.get(id=question_id)
    answers = Answer.objects.filter(question=question)

    return render(request, 'question.html', {'question': question, 'answers': answers})