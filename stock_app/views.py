from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Category, Firm, Product, Purchases, Sales, Brand
from .serializers import CategorySerializer, CategoryWithProductSerializer, FirmSerializer, ProductSerializer, PurchasesSerializer, SalesSerializer, BrandSerializer


class CategoryMVS(ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name"]

    def get_serializer_class(self):
        if "search" in self.request.query_params:
            return CategoryWithProductSerializer  # Serializer with products field
        return CategorySerializer  # Default serializer without products


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
