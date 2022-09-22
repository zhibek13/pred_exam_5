from rest_framework import serializers

from .models import Category, Item, Order


class CategorySerializer(serializers.ModelSerializer):
    category_username = serializers.ReadOnlyField()

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["profile", ]


class ItemSerializer(serializers.ModelSerializer):
    item_username = serializers.ReadOnlyField()

    class Meta:
        model = Item
        fields = "__all__"
        read_only_fields = ["profile", "category", ]


class OrderSerializer(serializers.ModelSerializer):
    order_username = serializers.ReadOnlyField()

    class Meta:
        model = Order
        fields = "__all__"
        read_only_fields = ["profile", "item"]
