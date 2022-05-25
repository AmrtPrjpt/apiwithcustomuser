from django.shortcuts import get_object_or_404
from rest_framework import generics, viewsets
from rest_framework.response import Response
from .models import Product
from .serializer import ProductSerializer
from rest_framework.permissions import (
    BasePermission,
    IsAuthenticatedOrReadOnly,
    IsAuthenticated,
    SAFE_METHODS,
)


class ProductUserWritePermissions(BasePermission):
    message = "Editing products is restricted only to the author."

    def has_object_permission(self, request, view, obj):

        if request.method in SAFE_METHODS:
            return True

        return obj.author == request.user


class ProductList(viewsets.ModelViewSet):
    permission_classes = [ProductUserWritePermissions]
    serializer_class = ProductSerializer

    def get_object(self, queryset=None, **kwargs):
        item = self.kwargs.get("pk")
        return get_object_or_404(Product, slug=item)

    # Define custom queryset
    def get_queryset(self):
        return Product.objects.all()


# class ProductList(viewsets.ViewSet):
#     permission_classes = [IsAuthenticated]
#     queryset = Product.objects.all()

#     def list(self, request):
#         serializer_class = ProductSerializer(self.queryset, many=True)
#         return Response(serializer_class.data)

#     def retrieve(self, request, pk=None):
#         product = get_object_or_404(self.queryset, pk=pk)
#         serializer_class = ProductSerializer(product)
#         return Response(serializer_class.data)


# class ProductList(generics.ListCreateAPIView):
#     permission_classes = [IsAuthenticatedOrReadOnly]
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer


# class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
#     permission_classes = [ProductUserWritePermissions]
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer
