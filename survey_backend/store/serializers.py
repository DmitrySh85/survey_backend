from rest_framework.fields import UUIDField
from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    ValidationError
)
from .models import Item, Order
from employees.models import Employee


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class OrderSerializer(ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"

    def create(self, validated_data):

        purchaser = validated_data["purchaser"]
        item = validated_data["item"]

        if purchaser.points < item.price:
            raise ValidationError("Insufficient points to purchase")

        order = Order.objects.create(
            purchaser=purchaser,
            item=item
        )
        purchaser.points -= item.price
        purchaser.save()

        return order

