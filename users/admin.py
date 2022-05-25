from django.contrib import admin
from .models import User
from django.contrib.auth.admin import UserAdmin

# Register your models here


class UserAdminConfig(UserAdmin):
    model = User
    search_fields = ("user_name",)
    list_display = (
        "user_name",
        "email",
        "is_staff",
        "is_active",
        "is_superuser",
    )
    ordering = ("-user_name",)
    fieldsets = (
        (None, {"fields": ("user_name", "email")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
        ("Personal", {"fields": ("about",)}),
    )
    add_fieldsets = (
        (None, {"fields": ("user_name", "email", "password1", "password2")}),
        ("Permissions", {"fields": ("is_staff", "is_active")}),
    )


admin.site.register(User, UserAdminConfig)
