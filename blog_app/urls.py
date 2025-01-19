from django.urls import path
from unicodedata import category

from . import views

app_name = "blog"
urlpatterns = [
    path("article/<int:pk>", views.articleDetail, name="ArticleDetail"),
    path("article/list", views.allArticles, name="allArticles"),
    path("category/<str:title>", views.allCategories, name="allCategories")
]
