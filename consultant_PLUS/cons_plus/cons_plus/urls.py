"""
URL configuration for cons_plus project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from second_help import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('repair/question/<int:question_id>/', views.show_question, name='show_repair_question'),
    path('product/question/<int:question_id>/', views.show_question, name='show_product_question'),
    path('solution/<int:solution_id>/', views.show_solution, name='show_solution'),
    path('articles/<str:article_name>/', views.show_article, name='show_article'),
    path('update_score/', views.update_score, name='update_score'),
    path('tag_search/', views.tag_search, name='tag_search'),
]
