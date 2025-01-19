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


class Article(models.Model):
    class Meta:
        verbose_name = "Article"
        verbose_name_plural = "Articles"
        db_table = "Article"

    category = models.ManyToManyField(Category)
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=User.objects.all().first().id)
    title = models.CharField(max_length=50, verbose_name="Article Title")
    tag = models.CharField(max_length=50, verbose_name="Article Tag", default="")
    body = models.TextField(max_length=255, verbose_name="Article Information")
    image = models.ImageField(upload_to="blog/images", verbose_name="Article Image")
    created = models.DateTimeField(auto_now_add=True, verbose_name="Create time of Article")
    updated = models.DateTimeField(auto_now=True, verbose_name="Update time of Aricle")

    def __str__(self):
        return self.title + " - " + self.body[:30]

    def get_url(self):
        return reverse("blog:ArticleDetail", kwargs={"pk": self.id})

    def get_author_url(self):
        return reverse("account_app:UserProfile",
                       kwargs={"slug": slugify(self.author.first_name + " " + self.author.username)})
