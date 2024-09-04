from rest_framework.viewsets import ModelViewSet

from .models import Category, Firm, Product, Purchases, Sales, Brand
from .serializers import CategorySerializer, FirmSerializer, ProductSerializer, PurchasesSerializer, SalesSerializer, BrandSerializer


class CategoryMVS(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class FirmMVS(ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer


class ProductMVS(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class PurchasesMVS(ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer


class SalesMVS(ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer


class BrandMVS(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
