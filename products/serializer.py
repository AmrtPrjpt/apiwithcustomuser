from rest_framework import serializers
from .models import Products


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ("id", "name", "price", "description", "author")
        model = Products
