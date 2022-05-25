from django.urls import path

from products.models import Products

from .views import ProductList, ProductDetail

app_name = "products"

urlpatterns = [
    path("<int:pk>/", ProductDetail.as_view(), name="listdetail"),
    path("", ProductList.as_view(), name="listcreate"),
]
