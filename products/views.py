from email import message
from rest_framework import generics
from .models import Product
from .serializer import ProductSerializer
from rest_framework.permissions import (
    BasePermission,
    IsAuthenticatedOrReadOnly,
    SAFE_METHODS,
)


class ProductUserWritePermissions(BasePermission):
    message = "Editing products is restricted only to the author."

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class ProductList(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticatedOrReadOnly]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [ProductUserWritePermissions]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
