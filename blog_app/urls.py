from django.urls import path
from . import views

app_name = "blog"
urlpatterns = [
    path("article/<int:pk>", views.articleDetail, name="ArticleDetail"),
    path("article/list", views.allArticles, name="allArticles"),
]
