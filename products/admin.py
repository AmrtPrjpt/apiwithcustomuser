from django.contrib import admin

# from .models import Product
from . import models

# Register your models here.
@admin.register(models.Product)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ("name", "id", "price", "author")
