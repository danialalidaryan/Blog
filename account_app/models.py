from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from .validator import Validator as V


# *** Account Model ***
class Religion(models.Model):
    class Meta:
        verbose_name = "دین"
        verbose_name_plural = "ادیان"
        db_table = "Religion"

    Title = models.CharField(
        max_length=50,
        verbose_name="نام دین",
        db_column="نام دین",
        help_text="نام دین را بنویسید",
    )

    def __str__(self):
        return self.Title


class UsersManager(BaseUserManager):
    def create_user(self, UserName, Password=None):
        if not UserName:
            raise ValueError('The Username field must be set')
        user = self.model(username=UserName)
        user.set_password(Password)
        user.save(using=self._db)
        return user


def create_superuser(self, UserName, Password):
    user = self.create_user(UserName, Password)
    user.is_superuser = True
    user.is_staff = True
    user.is_admin = True
    user.save(using=self._db)
    return user

class Users(AbstractBaseUser):
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
        db_table = "Users"
        unique_together = ['FirstName', 'LastName']

    GENDER_CHOICER = (
        ("Male", "male"),
        ("Female", "female")
    )

    UserName = models.CharField(
        primary_key=True,
        unique=True,
        max_length=100,
        db_column="نام کاربری",
        help_text="فیلد اجباری*. نام کاربری کاربر را بنویسید",
    )

    Password = models.CharField(
        max_length=100,
        db_column="رمز عبور",
        help_text="فیلد اجباری*. رمز عبور کاربر را بنویسید",
    )

    FirstName = models.CharField(
        max_length=100,
        verbose_name="نام",
        db_column="نام",
        help_text="فیلد اجباری*. نام کاربر را بنویسید",
    )

    LastName = models.CharField(
        max_length=100,
        verbose_name="نام خانوادگی",
        db_column="نام خانوادگی",
        help_text="فیلد اجباری*. نام خانوادگی کاربر را بنویسید",
    )

    NationalCode = models.CharField(
        null=True,
        blank=True,
        unique=True,
        max_length=10,
        validators=[V.NationalCode_Validator],
        verbose_name="کد ملی",
        db_column="کد ملی",
        help_text="فیلد اجباری*. کد ملی کاربر را بنویسید",
    )

    BirthDate = models.DateField(
        null=True,
        blank=True,
        verbose_name='تاریخ تولد',
        db_column="تاریخ تولد",
        help_text="تاریخ تولد کاربر را بنویسید",
    )

    Gender = models.CharField(
        choices=GENDER_CHOICER,
        max_length=6,
        verbose_name="جنسیت",
        db_column="جنسیت",
        help_text="فیلد اجباری*. جنسیت کاربر را بنویسید",
    )

    About = models.CharField(
        null=True,
        blank=True,
        max_length=500,
        verbose_name="درباره من",
        db_column="درباره من",
        help_text="درباره کاربر بنویسید",
    )

    FatherName = models.CharField(
        null=True,
        blank=True,
        max_length=100,
        verbose_name="نام پدر",
        db_column="نام پدر",
        help_text="نام پدر کاربر را بنویسید",
    )

    Image = models.ImageField(
        null=True,
        blank=True,
        upload_to="accounts/profile-images",
        verbose_name="عکس کاربر",
        db_column="عکس",
        help_text="عکس کاربر را وارد کنید",
    )

    Religion = models.ForeignKey(
        Religion,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="Users"
    )

    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    last_login = models.DateTimeField(auto_now=True)
    date_joined = models.DateTimeField(auto_now_add=True)

    objects = UsersManager()

    REQUIRED_FIELDS = ['Password']
    USERNAME_FIELD = 'UserName'

    def __str__(self):
        return self.UserName + "|" + self.NationalCode

    def get_full_name(self):
        return self.FirstName + " " + self.LastName


class EmailAddress(models.Model):
    class Meta:
        verbose_name = "آدرس پست الکترونیکی"
        verbose_name_plural = "آدرس های پست الکترونیکی"
        db_table = "EmailAddress"
        unique_together = ['User', 'Email']

    TYPE_CHOICER = (
        ("Phone", "phone"),
        ("Home", "home"),
        ("Work", "work"),
        ("School", "school"),
    )

    Email = models.EmailField(
        verbose_name="آدرس پست الکترونیکی",
        db_column="ایمیل",
        help_text="ایمیل کاربر را بنویسید",
    )
    Type = models.CharField(
        blank=True,
        null=True,
        choices=TYPE_CHOICER,
        max_length=6,
        verbose_name="نوع ایمیل",
        db_column="نوع ایمیل",
        help_text="نوع ایمیل کاربر را بنویسید",
    )

    User = models.ForeignKey(
        "Users",
        verbose_name="کاربر",
        db_column="کاربر",
        help_text="ایمیل کدام کاربر است",
        on_delete=models.CASCADE,
        related_name="Emails"
    )

    Is_Default = models.BooleanField(
        default=True,
        verbose_name="آیا پیش فرض است؟",
        db_column="ایمیل پیش فرض",
        help_text="بگویید که آیا این ایمیل پیش فرض کاربر است یا خیر",
    )

    def __str__(self):
        if self.Type == None:
            return self.Email
        else:
            return self.Email + "|" + self.Type


class PhoneNumber(models.Model):
    class Meta:
        verbose_name = "شماره تماس"
        verbose_name_plural = "شماره های تماس"
        db_table = "PhoneNumber"

    TYPE_CHOICER = (
        ("Phone", "phone"),
        ("Home", "home"),
        ("Work", "work"),
        ("School", "school"),
    )

    TelNumber = models.CharField(
        max_length=11,
        verbose_name="شماره تماس",
        db_column="شماره تماس",
        help_text="شماره تماس کاربر را بنویسید",
    )

    Type = models.CharField(
        choices=TYPE_CHOICER,
        max_length=6,
        blank=True,
        null=True,
        verbose_name="نوع شماره تماس",
        db_column="نوع شماره تماس",
        help_text="نوع شماره تماس کاربر را بنویسید",
    )

    User = models.ForeignKey(
        "Users",
        verbose_name="کاربر",
        db_column="کاربر",
        help_text="شماره تماس کدام کاربر است",
        on_delete=models.CASCADE,
        related_name='phoneNumbers'
    )

    IsDefault = models.BooleanField(
        default=True,
        verbose_name="آیا پیش فرض است؟",
        db_column="شماره تماس پیش فرض",
        help_text="بگویید که آیا این شماره تماس پیش فرض کاربر است یا خیر",
    )


class Role(models.Model):
    class Meta:
        verbose_name = "سمت"
        verbose_name_plural = "سمت ها"
        db_table = "Role"

    Title = models.CharField(
        max_length=50,
        verbose_name="سمت کاربر",
        db_column="سمت",
        help_text="سمت کاربر را بنویسید",
    )

    User = models.ForeignKey(
        Users,
        on_delete=models.CASCADE,
        related_name="Roles",
        verbose_name="کاربر",
        db_column="کاربر",
        help_text="سمت کدام کاربر است",
    )
# *** Account Model ***
