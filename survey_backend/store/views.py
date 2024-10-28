from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.permissions import IsAuthenticated
from .serializers import ItemSerializer, OrderSerializer
from .models import Item, Order


class ItemListAPIView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = ItemSerializer
    queryset = Item.objects.all()


class OrderCreateAPIView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = OrderSerializer
    queryset = Order.objects.all()