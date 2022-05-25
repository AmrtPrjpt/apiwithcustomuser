from django.urls import path
from .views import ProductList, ProductDetail

app_name = "product"

urlpatterns = [
    path("<int:pk>/", ProductDetail.as_view(), name="listdetail"),
    path("", ProductList.as_view(), name="listcreate"),
]
