from django.db import models
from django.conf import settings
from django_extensions.db.fields import AutoSlugField
from django.utils import timezone


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=0.00)
    description = models.TextField(blank=True)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="product"
    )
    published = models.DateTimeField(default=timezone.now)
    slug = AutoSlugField(max_length=50, unique=True, populate_from=["name"])

    class Meta:
        ordering = ("-name",)

    def __str__(self):
        return self.name
