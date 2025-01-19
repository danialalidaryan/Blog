from django.db import models
from django.utils import timezone
from django.core.validators import RegexValidator
from django.contrib.auth.models import User
from django.utils.text import slugify
from django.urls import reverse


class Person(models.Model):
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "Persons"
        db_table = "Person"
        abstract = True
        unique_together = ['nationalCode', 'name']

    name = models.CharField(
        max_length=50,
        blank=False,
        null=False,
        verbose_name="First Name",
        db_column="First_Name",
        db_comment="First Name of person",
        default="Johan",
        help_text="enter person first name on this field",
    )
    gender = models.BooleanField(
        default=True,
        choices={
            True: "Male",
            False: "Female"
        }
    )
    nationalCode = models.CharField(
        max_length=10,
        unique=True,
        primary_key=True,
        validators=[
            RegexValidator(
                regex=r'^\d{10}$',
                message="National Code Have to be 10 length of Numbers",
                code=None,
                inverse_match=None,
                flags=None,
            )
        ]
    )
    pub_date = models.DateTimeField(
        editable=False,
        default=timezone.now
    )
    update_date = models.DateField(
        editable=False,
        default=timezone.now
    )


class FootballPlayer(Person):
    class Meta:
        verbose_name = "Football Player"
        verbose_name_plural = "Football Players"
        db_table = "Football Player"
        unique_together = ['name', 'shirtNumber']

    shirtNumber = models.PositiveSmallIntegerField(
        unique_for_year='pub_date',
        help_text="The Number That Shows in Player T-shirt"
    )


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, blank=True, null=True)
    nCode = models.CharField(max_length=11, unique=True, default=0)
    slug = models.SlugField(blank=True)
    pub_date = models.DateTimeField(
        default=timezone.now
    )
    update_date = models.DateField(
        default=timezone.now
    )

    def __str__(self):
        return self.user.first_name

    def get_url(self):
        return reverse("account_app:UserProfile", kwargs={"slug": self.slug})

    def save(self):
        self.slug = slugify(self.user.first_name + " " + self.user.username)
        super(Profile, self).save()


class TestManager(models.Manager):
    def is_published(self):
        return self.filter(published=True)

    def counter(self):
        return len(self.all())

    def printAll(self):
        for item in self.all():
            print(item)

    def auto_create(self, counter):
        flag = True
        for count in range(counter):
            if flag:
                flag = False
            else:
                flag = True
            Test(title="This is New Test", description="Put your description here", published=flag).save()


class Test(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=255)
    published = models.BooleanField(default=False)
    objects = TestManager()

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.title = self.title.replace(" ", ".")
        self.description = self.description.upper()
        super(Test, self).save(args, kwargs)
