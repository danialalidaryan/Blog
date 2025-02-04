from django.shortcuts import render, get_object_or_404, HttpResponse
from .models import Post, Category, PostTag
import urllib.parse
from django.core.paginator import Paginator

def postDetail(request, pk = 1):
    post = get_object_or_404(Post, id = pk)
    return render(request, "Post/post-details.html", context={
        "post": post,
    })

def allPosts(request, page = 1):
    paginator = Paginator(Post.objects.all(), 2)
    return render(request, "Post/allArticles.html", context={
        "Posts": paginator.get_page(page),
    })

def allCategories(request, title, page = 1):
    decoded_title = urllib.parse.unquote(title)
    category = get_object_or_404(Category, Title = decoded_title)
    paginator = Paginator(category.Posts.all(), 2)
    return render(request, "Post/allCategories.html", context={
        "Posts": paginator.get_page(page),
        "Post_Title": decoded_title,
        "Header":"Categories"
    })

def allTags(request, title, page):
    decoded_title = urllib.parse.unquote(title)
    tag = get_object_or_404(PostTag, Title = decoded_title)
    paginator = Paginator(tag.Posts.all(), 2)
    return render(request, "Post/allCategories.html", context={
        "Posts":paginator.get_page(page),
        "Post_Title": title,
        "Header": "Tags"
    })
