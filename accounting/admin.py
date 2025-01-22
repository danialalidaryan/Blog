from django.contrib import admin
from django.urls import reverse
from django.utils.html import format_html

from .models import *


# ***** کاربران *****
class CustomeUserAdmin(admin.ModelAdmin):
    list_display = ('UserName', 'email_link', 'role_link', 'grade_link', 'is_superuser', 'is_active')
    list_filter = ('is_staff', 'is_active')
    search_fields = ('NationalCode','UserName')
    fieldsets = (
        ('Personal Info',{
            'fields':(
                'UserName',
                'password',
                'FirstName',
                'LastName',
                'NationalCode',
                'FatherName',
                'BirthDate',
                'Gender',
                'About',
                'Image',
            ),
            'classes': ('collapse',)
        }),

        ('Email Info', {
            'fields': ('Email',),
            'classes': ('collapse',)
        }),

        ('Professional Info',{'fields':('Role','Grade','Religion'),
                              'classes':('collapse',)}),

        ('System Info',{
            'fields':(
                'is_superuser',
                'is_staff',
                'is_admin',
                'is_active',
            ),
            'classes': ('collapse',)
        })
    )
    actions = ['make_superuser','make_plain_user', 'active_user', 'disable_user']
    def make_superuser(self, request, queryset):
        queryset.update(is_superuser=True, is_staff = True, is_admin = True, is_active = True)
    make_superuser.short_description = f"تبدیل {CustomeUser._meta.verbose_name} به ادمین"

    def make_plain_user(self, request, queryset):
        queryset.update(is_superuser=False, is_staff = False, is_admin = False, is_active = True)
    make_plain_user.short_description = f"تبدیل {CustomeUser._meta.verbose_name} به {CustomeUser._meta.verbose_name}  ساده"

    def disable_user(self, request, queryset):
        queryset.update(is_active=False)
    disable_user.short_description = f"تبدیل {CustomeUser._meta.verbose_name} به {CustomeUser._meta.verbose_name} غیر فعال"

    def active_user(self, request, queryset):
        queryset.update(is_active=True)
    active_user.short_description = f"تبدیل {CustomeUser._meta.verbose_name} به {CustomeUser._meta.verbose_name}  فعال"

    def email_link(self, obj):
        if obj.Email:
            url = reverse('admin:accounting_emailaddress_change', args=[obj.Email.id])
            return format_html('<a href="{}">{}</a>', url, obj.Email.Email)
        return "No Email"
    email_link.short_description = "Email"

    def role_link(self, obj):
        if obj.Role:
            url = reverse('admin:accounting_role_change', args=[obj.Role.id])
            return format_html('<a href="{}">{}</a>', url, obj.Role.Title)
        return "No Role"
    role_link.short_description = "Role"

    def grade_link(self, obj):
        if obj.Grade:
            url = reverse('admin:accounting_grade_change', args=[obj.Grade.id])
            return format_html('<a href="{}">{}</a>', url, obj.Grade.Title)
        return "No Grade"
    grade_link.short_description = "Grade"
admin.site.register(CustomeUser, CustomeUserAdmin)

# ***** ایمیل *****
admin.site.register(EmailAddress)

# ***** سمت ها *****
admin.site.register(Role)

# ***** ادیان *****
admin.site.register(Religion)

# ***** رتبه ها *****
admin.site.register(Grade)