from rest_framework import serializers
from .models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "price", "description", "author", "published", "slug")
        model = Product
