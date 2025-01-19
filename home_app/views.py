from django.shortcuts import render
from blog_app.models import Article, Category, Content
from account_app.models import Test, Profile


def showHome(request):
    # print(Test.objects.counter())
    # Test.objects.auto_create(50)
    # Test.objects.all().delete()
    # print(reverse("blog:ArticleDetail",kwargs={"pk":1}))

    return render(request, 'home_app/index.html', context={
        "Articles": Article.objects.all(),
        "Profiles": Profile.objects.all(),
    })


def sidebar(request):
    return render(request, "sidebar.html", {"Category": Category.objects.all(),
                                            "Contents": Content.objects.all()})