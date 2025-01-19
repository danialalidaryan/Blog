import datetime

from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.text import slugify

# Create your models here.
class Category(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    title = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.title

class Content(models.Model):
    class Meta:
        verbose_name = "محتوا"
        verbose_name_plural = "محتوا ها"
        ordering = ["created"]


    title = models.CharField(max_length=25, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Article(models.Model):
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        db_table = "Article"

    category = models.ManyToManyField(Category, related_name="Articles")
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.all().first().id)
    content = models.ForeignKey(Content,on_delete=models.SET_DEFAULT, default=1, verbose_name="Article Content")
    tag = models.CharField(max_length=50, verbose_name="Article Tag", default="")
    body = models.TextField(max_length=255, verbose_name="Article Information")
    image = models.ImageField(upload_to="blog/images", default="blog/images/default.jfif", verbose_name="Article Image")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Create time of Article")
    updated = models.DateTimeField(auto_now=True, verbose_name="Update time of Aricle")

    def __str__(self):
        return self.content.title + " - " + self.author.username

    def get_url(self):
        return reverse("blog:ArticleDetail", kwargs={"pk": self.id})

    def get_author_url(self):
        return reverse("account_app:UserProfile",
                       kwargs={"slug": slugify(self.author.first_name + " " + self.author.username)})

