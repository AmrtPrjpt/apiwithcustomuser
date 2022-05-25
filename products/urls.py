from django.urls import path
from .views import ProductList
from rest_framework.routers import DefaultRouter

app_name = "product"

router = DefaultRouter()
router.register("", ProductList, basename="product")
urlpatterns = router.urls


# urlpatterns = [
#     # path("<int:pk>/", ProductDetail.as_view(), name="listdetail"),
#     # path("", ProductList.as_view(), name="listcreate"),
# ]
