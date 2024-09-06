from rest_framework import serializers

from .models import Category, Firm, Product, Purchases, Sales, Brand


class CategorySerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    product_count = serializers.SerializerMethodField()
    total_stock = serializers.SerializerMethodField()

    class Meta:
        model = Category
        fields = "__all__"
        read_only_fields = ["id", "created_date",
                            "updated_date", "user", "user_id"]

    def get_product_count(self, obj):
        return obj.product_category.count()

    def get_total_stock(self, obj):
        total_stock = sum(
            [product.stock for product in obj.product_category.all()])
        return total_stock


class FirmSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)

    class Meta:
        model = Firm
        fields = "__all__"
        read_only_fields = ["id", "created_date",
                            "updated_date", "user", "user_id"]


class BrandSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    category_name = serializers.SerializerMethodField()

    class Meta:
        model = Brand
        fields = "__all__"
        read_only_fields = ["id", "created_date",
                            "updated_date", "user", "user_id"]

    def get_category_name(self, obj):
        return [category.name for category in obj.category.all()]


class ProductSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    brand = serializers.StringRelatedField(read_only=True)
    brand_id = serializers.IntegerField()
    category = serializers.StringRelatedField(read_only=True)
    category_id = serializers.IntegerField()

    class Meta:
        model = Product
        fields = "__all__"
        read_only_fields = ["id", "created_date",
                            "updated_date", "user", "user_id", "brand", "category", "stock"]


# For showing the details when search filter is used
class CategoryWithProductSerializer(CategorySerializer):
    products = ProductSerializer(
        many=True, read_only=True, source="product_category")

    class Meta(CategorySerializer.Meta):
        fields = "__all__"


class PurchasesSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    firm = serializers.StringRelatedField(read_only=True)
    firm_id = serializers.IntegerField()
    brand = serializers.StringRelatedField(read_only=True)
    brand_id = serializers.IntegerField()
    product = serializers.StringRelatedField(read_only=True)
    product_id = serializers.IntegerField()
    category = serializers.StringRelatedField(
        source="product.category", many=True, read_only=True)

    class Meta:
        model = Purchases
        fields = "__all__"
        read_only_fields = ["id", "price_total",
                            "created_date", "updated_date", "user", "user_id", "firm", "brand", "product", "category"]


class SalesSerializer(serializers.ModelSerializer):
    user = serializers.StringRelatedField(read_only=True)
    user_id = serializers.IntegerField(read_only=True)
    product = serializers.StringRelatedField(read_only=True)
    product_id = serializers.IntegerField()
    brand = serializers.StringRelatedField(read_only=True)
    brand_id = serializers.IntegerField()

    class Meta:
        model = Sales
        fields = "__all__"
        read_only_fields = ["id", "price_total",
                            "created_date", "updated_date", "user", "user_id", "product", "brand"]

    def validate(self, data):
        product_id = data.get('product_id')

        if product_id is None:
            raise serializers.ValidationError("Product ID is required.")

        # Retrieving the product instance using the product_id
        try:
            product = Product.objects.get(id=product_id)
        except Product.DoesNotExist:
            raise serializers.ValidationError("Invalid product ID.")

        # Checking stock availability
        if product.stock < data.get('quantity', 0):
            raise serializers.ValidationError(
                "You do not have enough stock to handle this operation.")

        return data
