# Generated by Django 5.1.5 on 2025-02-03 12:28

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='EmailAddress',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Email', models.EmailField(db_column='ایمیل', help_text='ایمیل کاربر را بنویسید', max_length=254, unique=True, verbose_name='آدرس پست الکترونیکی')),
                ('Type', models.CharField(choices=[('Home', 'home'), ('Work', 'work'), ('School', 'school')], db_column='نوع ایمیل', default='Work', help_text='نوع ایمیل کاربر را بنویسید', max_length=6, verbose_name='نوع ایمیل')),
                ('Is_Default', models.BooleanField(db_column='ایمیل پیش فرض', default=False, help_text='بگویید که آیا این ایمیل پیش فرض کاربر است یا خیر', verbose_name='آیا پیش فرض است؟')),
            ],
            options={
                'verbose_name': 'آدرس پست الکترونیکی',
                'verbose_name_plural': 'آدرس های پست الکترونیکی',
                'db_table': 'account_EmailAddress',
            },
        ),
        migrations.CreateModel(
            name='Grade',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(db_column='نام رتبه', help_text='نام رتبه را بنویسید', max_length=50, unique=True, verbose_name='عنوان رتبه')),
                ('description', models.TextField(blank=True, db_column='توضیحات', help_text='توضیحات را بنویسید', max_length=500, null=True, verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'رتبه',
                'verbose_name_plural': 'رتبه ها',
                'db_table': 'account_Grade',
            },
        ),
        migrations.CreateModel(
            name='Religion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(db_column='نام دین', help_text='نام دین را بنویسید', max_length=50, unique=True, verbose_name='عنوان دین')),
                ('description', models.TextField(blank=True, db_column='توضیحات', help_text='توضیحات را بنویسید', max_length=500, null=True, verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'دین',
                'verbose_name_plural': 'ادیان',
                'db_table': 'account_Religion',
            },
        ),
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Title', models.CharField(db_column='سمت', help_text='عنوان سمت را بنویسید', max_length=50, unique=True, verbose_name='عنوان سمت')),
                ('description', models.TextField(blank=True, db_column='توضیحات', help_text='توضیحات را بنویسید', max_length=500, null=True, verbose_name='توضیحات')),
            ],
            options={
                'verbose_name': 'سمت',
                'verbose_name_plural': 'سمت ها',
                'db_table': 'account_Role',
            },
        ),
        migrations.CreateModel(
            name='CustomeUser',
            fields=[
                ('UserName', models.CharField(db_column='نام کاربری', help_text='فیلد اجباری*. نام کاربری کاربر را بنویسید', max_length=100, unique=True, verbose_name='نام کاربری')),
                ('password', models.CharField(db_column='رمز عبور', help_text='لطفاً رمز عبور خود را وارد کنید.', max_length=128, verbose_name='رمز عبور')),
                ('is_active', models.BooleanField(default=True, verbose_name='is Active')),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False, verbose_name='is Staff')),
                ('is_superuser', models.BooleanField(default=False)),
                ('last_login', models.DateTimeField(auto_now=True)),
                ('temp_email', models.EmailField(blank=True, max_length=254, null=True, unique=True, verbose_name='Email')),
                ('FirstName', models.CharField(db_column='نام', help_text='فیلد اجباری*. نام کاربر را بنویسید', max_length=100, verbose_name='نام')),
                ('LastName', models.CharField(db_column='نام خانوادگی', help_text='فیلد اجباری*. نام خانوادگی کاربر را بنویسید', max_length=100, verbose_name='نام خانوادگی')),
                ('NationalCode', models.CharField(db_column='کد ملی', help_text='فیلد اجباری*. کد ملی کاربر را بنویسید', max_length=10, primary_key=True, serialize=False, unique=True, verbose_name='کد ملی')),
                ('BirthDate', models.DateField(blank=True, db_column='تاریخ تولد', help_text='تاریخ تولد کاربر را بنویسید', null=True, verbose_name='تاریخ تولد')),
                ('Gender', models.CharField(choices=[('male', 'Male'), ('female', 'Female')], db_column='جنسیت', default='male', help_text='فیلد اجباری*. جنسیت کاربر را بنویسید', max_length=6, verbose_name='جنسیت')),
                ('About', models.TextField(blank=True, db_column='درباره من', help_text='درباره کاربر بنویسید', max_length=500, null=True, verbose_name='درباره من')),
                ('FatherName', models.CharField(blank=True, db_column='نام پدر', help_text='نام پدر کاربر را بنویسید', max_length=100, null=True, verbose_name='نام پدر')),
                ('Image', models.ImageField(blank=True, db_column='عکس', help_text='عکس کاربر را وارد کنید', null=True, upload_to='Accounting/profile-images', verbose_name='عکس کاربر')),
                ('Email', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Users', to='Accounting.emailaddress', verbose_name='Email')),
                ('Grade', models.OneToOneField(blank=True, db_column='رتبه', help_text='رتبه در سمت کاربر را وارد کنید', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Users', to='Accounting.grade', verbose_name='رتبه')),
                ('Religion', models.OneToOneField(blank=True, db_column='دین', help_text='دین کاربر را وارد کنید', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Users', to='Accounting.religion', verbose_name='دین')),
                ('Role', models.OneToOneField(blank=True, db_column='سمت', help_text='سمت کاربر را وارد کنید', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Users', to='Accounting.role', verbose_name='سمت')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'کاربر',
                'verbose_name_plural': 'کاربران',
                'db_table': 'account_CustomeUser',
                'unique_together': {('FirstName', 'LastName')},
            },
        ),
        migrations.AddField(
            model_name='emailaddress',
            name='User',
            field=models.ForeignKey(blank=True, db_column='کاربر', help_text='ایمیل کدام کاربر است', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Emails', to=settings.AUTH_USER_MODEL, verbose_name='کاربر'),
        ),
        migrations.AlterUniqueTogether(
            name='emailaddress',
            unique_together={('User', 'Email')},
        ),
    ]
