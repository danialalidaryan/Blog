from django.shortcuts import render
from blog_app.models import Article, Category, Content
from account_app.models import Profile

def showHome(request):
    return render(request, 'home_app/index.html', context={
        "Articles": Article.objects.all(),
        "Profiles": Profile.objects.all(),
    })


def sidebar(request):
    return render(request, "sidebar.html", {"Category": Category.objects.all(),
                                            "Contents": Content.objects.all()})