from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse

from .models import Post, Category, PostTag, Comment
from Accounting.models import CustomeUser
import urllib.parse
from django.core.paginator import Paginator


def postDetail(request, pk=1):
    post = get_object_or_404(Post, id=pk)
    if request.method == "POST":
        has_parent = request.POST.get("parent")
        if has_parent == "None":
            print("Hello")
            Comment.objects.create(
                User=get_object_or_404(CustomeUser, NationalCode=request.user.NationalCode),
                Post=get_object_or_404(Post, id=pk),
                Body=request.POST.get("body"),
                Parent=None,
            )
        else:
            Comment.objects.create(
                User=get_object_or_404(CustomeUser, NationalCode=request.user.NationalCode),
                Post=get_object_or_404(Post, id=pk),
                Body=request.POST.get("body"),
                Parent=get_object_or_404(Comment, id=request.POST.get("parent")),
            )
        return redirect(post.get_url())

    return render(request, "Post/post-details.html", context={
        "post": post,
    })


def allPosts(request, page=1):
    paginator = Paginator(Post.objects.all(), 2)
    return render(request, "Post/allArticles.html", context={
        "Posts": paginator.get_page(page),
    })


def search(request, page=1):
    title = request.GET.get('title')
    finder = Post.objects.filter(Title__icontains=title)
    paginator = Paginator(finder, 2)
    return render(request, "Post/allArticles.html", context={
        "Posts": paginator.get_page(page),
    })


def allCategories(request, title, page=1):
    decoded_title = urllib.parse.unquote(title)
    category = get_object_or_404(Category, Title=decoded_title)
    paginator = Paginator(category.Posts.all(), 2)
    return render(request, "Post/allCategories.html", context={
        "Posts": paginator.get_page(page),
        "Post_Title": decoded_title,
        "Header": "Categories"
    })


def allTags(request, title, page):
    decoded_title = urllib.parse.unquote(title)
    tag = get_object_or_404(PostTag, Title=decoded_title)
    paginator = Paginator(tag.Posts.all(), 2)
    return render(request, "Post/allCategories.html", context={
        "Posts": paginator.get_page(page),
        "Post_Title": title,
        "Header": "Tags"
    })
