from pickle import FALSE
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin


class CustomeUserManager(BaseUserManager):
    def create_user(self, UserName, temp_email, FirstName, LastName, NationalCode, Gender, password=None,
                    **extra_fields):
        if not temp_email:
            raise ValueError("The user must have an Email.")
        if not password:
            raise ValueError("Password Neded")

        # قبل از ایجاد یوزر ایمیل رو ایجاد میکنیم
        email_instance = EmailAddress.objects.create(User=None, Email=self.normalize_email(temp_email), Is_Default=True)

        user = self.model(
            UserName=UserName,
            FirstName=FirstName,
            LastName=LastName,
            NationalCode=NationalCode,
            Gender=Gender,
            **extra_fields
        )
        extra_fields.setdefault('is_active', True)
        if password:
            user.set_password(password)
        user.Email = email_instance
        user.save(using=self._db)

        # حالا که یوزر ایجاد شد ایمیل رو به یوزر وصل میکنیم
        email_instance.User = user
        email_instance.save()
        return user

    def create_superuser(self, UserName, temp_email, FirstName, LastName, NationalCode, Gender, password=None,
                         **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self.create_user(
            UserName=UserName,
            temp_email=temp_email,
            FirstName=FirstName,
            LastName=LastName,
            NationalCode=NationalCode,
            Gender=Gender,
            password=password,
            **extra_fields
        )

class CustomeUser(AbstractBaseUser, PermissionsMixin):
    class Meta:
        verbose_name = "کاربر"
        verbose_name_plural = "کاربران"
        db_table = "account_CustomeUser"
        unique_together = ['FirstName', 'LastName']

    GENDER_CHOICER = (
        ("Male", "male"),
        ("Female", "female")
    )

    # ***** System Info *****
    UserName = models.CharField(
        unique=True,
        max_length=100,
        verbose_name="نام کاربری",
        db_column="نام کاربری",
        help_text="فیلد اجباری*. نام کاربری کاربر را بنویسید",
    )
    password = models.CharField(
        max_length=128,
        verbose_name="رمز عبور",
        db_column="رمز عبور",
        help_text="لطفاً رمز عبور خود را وارد کنید.",
    )
    is_active = models.BooleanField(default=True, verbose_name="is Active")
    is_admin = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False, verbose_name="is Staff")
    is_superuser = models.BooleanField(default=False)
    last_login = models.DateTimeField(auto_now=True)

    # ***** Email *****
    temp_email = models.EmailField(
        unique=True,
        null=True,
        blank=True,
        verbose_name="Email",
    )
    Email = models.OneToOneField("EmailAddress", on_delete=models.CASCADE, related_name="Users", blank=True, null=True,
                                 verbose_name="Email")

    # ***** Personal Info *****
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
        primary_key=True,
        unique=True,
        max_length=10,
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
        default="male",
        max_length=6,
        verbose_name="جنسیت",
        db_column="جنسیت",
        help_text="فیلد اجباری*. جنسیت کاربر را بنویسید",
    )
    About = models.TextField(
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
    Role = models.OneToOneField(
        "Role",
        on_delete=models.SET_NULL,
        related_name="Users",
        null=True,
        blank=True,
        verbose_name="سمت",
        db_column="سمت",
        help_text="سمت کاربر را وارد کنید",
    )
    Religion = models.OneToOneField(
        "Religion",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="Users",
        verbose_name="دین",
        db_column="دین",
        help_text="دین کاربر را وارد کنید",
    )
    Grade = models.OneToOneField(
        "Grade",
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="Users",
        verbose_name="رتبه",
        db_column="رتبه",
        help_text="رتبه در سمت کاربر را وارد کنید",
    )

    # ***** Manager *****
    objects = CustomeUserManager()

    USERNAME_FIELD = "UserName"
    REQUIRED_FIELDS = ['temp_email', 'FirstName', 'LastName', 'NationalCode', 'Gender']

    def save(self, *args, **kwargs):
        if self.Email is not None:
            if self.Email.Is_Default:
                super().save(*args, **kwargs)
            else:
                self.Email.Is_Default = True
                print(f"Updating account_superuser {self.UserName}... OK")
                self.Email.save()
        else:
            print(f"Creating account_superuser {self.UserName}... OK")
        super().save(*args, **kwargs)

    def __str__(self):
        return self.get_fullname()

    def get_fullname(self):
        return self.FirstName + "\t" + self.LastName

class EmailAddress(models.Model):
    class Meta:
        verbose_name = "آدرس پست الکترونیکی"
        verbose_name_plural = "آدرس های پست الکترونیکی"
        db_table = "account_EmailAddress"
        unique_together = ['User', 'Email']

    TYPE_CHOICER = (
        ("Home", "home"),
        ("Work", "work"),
        ("School", "school"),
    )
    Email = models.EmailField(
        unique=True,
        verbose_name="آدرس پست الکترونیکی",
        db_column="ایمیل",
        help_text="ایمیل کاربر را بنویسید",
    )
    Type = models.CharField(
        choices=TYPE_CHOICER,
        default="Work",
        max_length=6,
        verbose_name="نوع ایمیل",
        db_column="نوع ایمیل",
        help_text="نوع ایمیل کاربر را بنویسید",
    )
    Is_Default = models.BooleanField(
        default=False,
        verbose_name="آیا پیش فرض است؟",
        db_column="ایمیل پیش فرض",
        help_text="بگویید که آیا این ایمیل پیش فرض کاربر است یا خیر",
    )
    User = models.ForeignKey(
        CustomeUser,
        null=True,
        blank=True,
        verbose_name="کاربر",
        db_column="کاربر",
        help_text="ایمیل کدام کاربر است",
        on_delete=models.CASCADE,
        related_name="Emails",
    )

    def save(self, *args, **kwargs):
        if self.Is_Default:
            EmailAddress.objects.filter(User=self.User, Is_Default=True).update(Is_Default=False)
            print(f"Updating/ Creating account_emailaddress {self.Email}... OK")
        else:
            print(f"Creating account_emailaddress {self.Email}... OK")
        super().save(*args, **kwargs)
        if self.User is not None:
            self.User.Email = self
            self.User.save()

    def __str__(self):
        return self.Email

class Role(models.Model):
    class Meta:
        verbose_name = "سمت"
        verbose_name_plural = "سمت ها"
        db_table = "account_Role"

    Title = models.CharField(
        unique=True,
        max_length=50,
        verbose_name="عنوان سمت",
        db_column="سمت",
        help_text="عنوان سمت را بنویسید",
    )

    description = models.TextField(max_length=500,
                                   blank=True,
                                   null=True,
                                   verbose_name="توضیحات",
                                   db_column="توضیحات",
                                   help_text="توضیحات را بنویسید",
                                   )

    def __str__(self):
        return self.Title

class Religion(models.Model):
    class Meta:
        verbose_name = "دین"
        verbose_name_plural = "ادیان"
        db_table = "account_Religion"

    Title = models.CharField(
        unique=True,
        max_length=50,
        verbose_name="عنوان دین",
        db_column="نام دین",
        help_text="نام دین را بنویسید",
    )
    description = models.TextField(max_length=500,
                                   blank=True,
                                   null=True,
                                   verbose_name="توضیحات",
                                   db_column="توضیحات",
                                   help_text="توضیحات را بنویسید",
                                   )

    def __str__(self):
        return self.Title

class Grade(models.Model):
    class Meta:
        verbose_name = "رتبه"
        verbose_name_plural = "رتبه ها"
        db_table = "account_Grade"

    Title = models.CharField(
        unique=True,
        max_length=50,
        verbose_name="عنوان رتبه",
        db_column="نام رتبه",
        help_text="نام رتبه را بنویسید",
    )
    description = models.TextField(max_length=500,
                                   blank=True,
                                   null=True,
                                   verbose_name="توضیحات",
                                   db_column="توضیحات",
                                   help_text="توضیحات را بنویسید",
                                   )

    def __str__(self):
        return self.Title
