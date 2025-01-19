from gc import get_objects
from django.shortcuts import render, get_object_or_404
from .models import Article, Category
from account_app.models import Profile

# Create your views here.

app_name = "articleDetail"


def articleDetail(request, pk):
    return render(request, "blog_app/post-details.html", context={
        "article": Article.objects.all().filter(id=pk)[0],
        "Profiles": Profile.objects.all(),
        "recentArticle": Article.objects.all().order_by('-created')[:3]
    })

def allArticles(request):
    return render(request, "blog_app/allArticles.html", context={
        "Articles": Article.objects.all()
    })

def allCategories(request, title = "Coding"):
    category = get_object_or_404(Category, title = title)
    return render(request, "blog_app/allArticles.html", context={
        "Articles": category.Articles.all()
    })