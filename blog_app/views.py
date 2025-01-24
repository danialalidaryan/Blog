from gc import get_objects
from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from Accounting.models import Profile
from django.core.paginator import Paginator

# Create your views here.

app_name = "articleDetail"


def articleDetail(request, pk = 1):
    return render(request, "blog_app/post-details.html", context={
        "article": Article.objects.all().filter(id=pk)[0],
        "Profiles": Profile.objects.all(),
        "recentArticle": Article.objects.all().order_by('-created')[:3]
    })

def allArticles(request, page = 1):
    paginator = Paginator(Article.objects.all(), 2)
    return render(request, "blog_app/allArticles.html", context={
        "Articles": paginator.get_page(page),
    })

def allCategories(request, title = "Coding", page = 1):
    category = get_object_or_404(Category, title = title)
    paginator = Paginator(category.Articles.all(), 2)
    return render(request, "blog_app/allCategories.html", context={
        "Articles": paginator.get_page(page),
        "title": title
    })
