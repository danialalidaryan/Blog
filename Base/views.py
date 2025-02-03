from django.shortcuts import render, HttpResponse
from Post.models import *


def showHome(request):
    Posts = Post.objects.all()
    return render(request, 'Base/index.html', context={
        "Posts": Posts,

    })


def sidebar(request):
    Categories = Category.objects.all()
    Tags = PostTag.objects.all()
    return render(request, "sidebar.html", {"Category": Categories, "Tag": Tags})
