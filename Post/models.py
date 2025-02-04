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


class PostTag(models.Model):
    Title = models.CharField(unique=True, max_length=50)

    def __str__(self):
        return self.Title


class SocialAddress(models.Model):
    Title = models.CharField(max_length=50)
    Post = models.ForeignKey("Post", on_delete=models.CASCADE, null=True, blank=True, related_name="Social")
    Address = models.CharField(max_length=255, null=True, blank=True)
    Comment = models.TextField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.Title


class Post(models.Model):
    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Posts"
        db_table = "Post"
    Title = models.CharField(max_length=100, unique=True, default="None")
    Category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="Posts", null=True)
    Author = models.ForeignKey(
        CustomeUser,
        null=True,
        blank=True,
        verbose_name="نویسنده",
        db_column="نویسنده",
        help_text="این پست برای کدام کاربر است",
        on_delete=models.CASCADE,
        related_name="Posts")
    Tag = models.ManyToManyField(PostTag, verbose_name="Post Content", related_name="Posts")
    Comment = models.TextField(verbose_name="Post Information")
    Image = models.ImageField(upload_to="Post/images", default="blog/images/default.jpg", verbose_name="Post Image")
    Banner = models.ImageField(upload_to="Post/images", verbose_name="Post Banner", null=True, blank=True )
    Created = models.DateTimeField(auto_now_add=True, verbose_name="Create time of Post")
    Updated = models.DateTimeField(auto_now=True, verbose_name="Update time of Post")

    def __str__(self):
        return self.Title + " - " + self.Author.UserName

    def get_url(self):
        return reverse("Post:postDetail", kwargs={"pk": self.id})

    def get_author_url(self):
        return reverse("Accounting:userProfile", kwargs={"pk": self.Author.UserName})

class Comment(models.Model):
    User = models.ForeignKey(CustomeUser, on_delete=models.CASCADE)
    Post = models.ForeignKey(Post,on_delete=models.CASCADE, related_name="Comments")
    Body = models.TextField()
    Parent = models.ForeignKey("self",on_delete=models.CASCADE, blank=True, null=True, related_name="Replies")
    Created = models.DateField(auto_now_add=True)

    def __str__(self):
        if self.Parent is not None:
            return f"Reply to {self.Parent.User.UserName}"
        else:
            return f"{self.User.UserName} | {self.Body[:20]}"

