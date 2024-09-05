from rest_framework import serializers

from .models import Category, Firm, Product, Purchases, Sales, Brand


class CategorySerializer(serializers.ModelSerializer):
    product_count = serializers.SerializerMethodField()
    total_stock = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["id", "created_date", "updated_date"]

    def get_product_count(self, obj):
        return obj.product_category.count()

    def get_total_stock(self, obj):
        total_stock = sum(
            [product.stock for product in obj.product_category.all()])
        return total_stock


class FirmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Firm
        fields = "__all__"
        read_only_fields = ["id", "created_date", "updated_date"]


class BrandSerializer(serializers.ModelSerializer):
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = "__all__"
        read_only_fields = ["id", "category_name",
                            "created_date", "updated_date"]

    def get_category_name(self, obj):
        return [category.name for category in obj.category.all()]


class ProductSerializer(serializers.ModelSerializer):
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    category = serializers.StringRelatedField()
    category_id = serializers.IntegerField()

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["id", "created_date", "updated_date"]


# For showing the details when search filter is used
class CategoryWithProductSerializer(CategorySerializer):
    products = ProductSerializer(
        many=True, read_only=True, source="product_category")

    class Meta(CategorySerializer.Meta):
        fields = "__all__"


class PurchasesSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()
    firm = serializers.StringRelatedField()
    firm_id = serializers.IntegerField()
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()

    class Meta:
        model = Purchases
        fields = "__all__"
        read_only_fields = ["id", "price_total",
                            "created_date", "updated_date"]


class SalesSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField()
    user_id = serializers.IntegerField()
    product = serializers.StringRelatedField()
    product_id = serializers.IntegerField()
    brand = serializers.StringRelatedField()
    brand_id = serializers.IntegerField()

    class Meta:
        model = Sales
        fields = "__all__"
        read_only_fields = ["id", "price_total",
                            "created_date", "updated_date"]
