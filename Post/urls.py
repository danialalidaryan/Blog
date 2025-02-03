from django.urls import path
# from unicodedata import category
from . import views
app_name = "Post"
urlpatterns = [
    path("<int:pk>", views.postDetail, name="postDetail"),
    path("post/list/<int:page>", views.allPosts, name="allPosts"),
    path("category/<path:title>/<int:page>", views.allCategories, name="allCategories"),
]
