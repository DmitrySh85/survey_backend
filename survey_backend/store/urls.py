from django.urls import path
from .views import ItemListAPIView, OrderCreateAPIView


urlpatterns = [
    path("items/", ItemListAPIView.as_view(), name="items"),
    path("order/", OrderCreateAPIView.as_view(), name="create_order"),
]
