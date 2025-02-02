from django.db import models
from Accounting.models import CustomeUser
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    Title = models.CharField(
        max_length=50
    )

    def __str__(self):
        return self.Title

class Tag(models.Model):
    Title = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.Title

class Social(models.Model):
    Title = models.CharField(max_length=50, unique=True)
    Address = models.CharField(max_length=255, null=True)
    Comment = models.TextField(max_length=500, null=True)

class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        db_table = "Post"

    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="Posts", null=True)
    Author = models.ForeignKey(CustomeUser, on_delete=models.CASCADE, default=CustomeUser.objects.all().first().NationalCode)
    Tag = models.ManyToManyField(Tag, verbose_name="Post Content", null=True)
    Social = models.ManyToManyField(Social, verbose_name="Post Social Address", null=True)
    Comment = models.TextField(max_length=255, verbose_name="Post Information")
    Image = models.ImageField(upload_to="Post/images", default="blog/images/default.jpg", verbose_name="Post Image")
    Created = models.DateTimeField(auto_now_add=True, verbose_name="Create time of Post")
    Updated = models.DateTimeField(auto_now=True, verbose_name="Update time of Post")

    def __str__(self):
        return self.Category.Title + " - " + self.Author.UserName

    def get_url(self):
        return reverse("Post:postDetail", kwargs={"pk": self.id})

    def get_author_url(self):
        return reverse("Accounting:userProfile", kwargs={"pk": self.Author.UserName})
