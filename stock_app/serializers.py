from rest_framework import serializers

from .models import Category, Firm, Product, Purchases, Sales, Brand


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["id"]


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = "__all__"
        read_only_fields = ["id"]


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = "__all__"
        read_only_fields = ["id"]


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["id", "created_date", "updated_date"]


class PurchasesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Purchases
        fields = "__all__"
        read_only_fields = ["id", "price_total",
                            "created_date", "updated_date"]


class SalesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sales
        fields = "__all__"
        read_only_fields = ["id", "price_total",
                            "created_date", "updated_date"]
