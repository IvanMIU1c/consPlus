from django.shortcuts import render
from django import forms
from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from .models import Question, Answer, Solution, Articles, SolutionScore, Tag, DocumentTemplates
from django.conf import settings
from .forms import TagSearchForm


def home(request):
    context = {'catgories': Question.objects.all()}

    if request.GET.get('gfg'):
        return redirect(f"/quiz/?gfg={request.GET.get('gfg')}")

    return render(request, 'home.html', context)


def show_question(request, question_id):
    question = Question.objects.get(id=question_id)
    answers = Answer.objects.filter(question=question)
    return render(request, 'question.html', {'question': question, 'answers': answers})


def show_solution(request, solution_id):
    solution = Solution.objects.get(id=solution_id)
    return render(request, 'solution.html', {'solution': solution})


def show_article(request, article_name):
    template_name = article_name
    return render(request, template_name)


def update_score(request):
    if request.method == 'POST':
        score = request.POST.get('score')
        solution_id = request.POST.get('id')
        score_sum = 0
        count = 1
        solution_scores = SolutionScore.objects.filter(solution_id=solution_id)
        for solution_score in solution_scores:
            score_sum += solution_score.score
            count += 1
        average_score = score_sum / count
        SolutionScore.objects.create(score=score, solution_id=solution_id, average_score=average_score)
        return redirect('home')


def tag_search(request):
    articles = Articles.objects.all()
    if request.method == 'GET':
        form = TagSearchForm(request.GET)
        if form.is_valid():
            tags = form.cleaned_data['tags']
            articles = Articles.objects.filter(tags__in=tags).distinct()
            return render(request, 'all_articles.html', {'articles': articles, 'form': form})
    else:
        form = TagSearchForm()

    return render(request, 'all_articles.html', {'articles': articles, 'form': form})


def all_articles(request):
    articles = Articles.objects.all()
    form = TagSearchForm(request.GET)
    return render(request, 'all_articles.html', {'articles': articles, 'form': form})


def all_docs(request):
    docs = DocumentTemplates.objects.all()
    form = TagSearchForm(request.GET)
    return render(request, 'all_docs.html', {'docs': docs, 'form': form})
