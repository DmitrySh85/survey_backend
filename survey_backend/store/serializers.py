from rest_framework.fields import UUIDField
from rest_framework.serializers import (
    ModelSerializer,
    IntegerField,
    ValidationError,
    PrimaryKeyRelatedField
)
from .models import Item, Order
from employees.models import Employee
from employees.serializers import EmployeeSerializer


class ItemSerializer(ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class OrderSerializer(ModelSerializer):

    item_details = ItemSerializer(source='item', read_only=True)
    purchaser_details = EmployeeSerializer(source='purchaser', read_only=True)


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
    
    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['item'] = representation.pop('item_details')
        representation['purchaser'] = representation.pop('purchaser_details')
        return representation

