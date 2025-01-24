from django.shortcuts import render
from blog_app.models import Article, Category, Content
from Accounting.models import Profile

def showHome(request):
    return render(request, 'Base/index.html', context={
        "Articles": Article.objects.all(),
        "Profiles": Profile.objects.all(),
    })


def sidebar(request):
    return render(request, "sidebar.html", {"Category": Category.objects.all(),
                                            "Contents": Content.objects.all()})