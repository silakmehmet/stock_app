from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from .permissions import IsAuthenticatedOrReadOnly
from .models import Category, Firm, Product, Purchases, Sales, Brand
from .serializers import CategorySerializer, CategoryWithProductSerializer, FirmSerializer, ProductSerializer, PurchasesSerializer, SalesSerializer, BrandSerializer
from .mixins import UserMixin


class CategoryMVS(UserMixin, ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name"]

    def get_serializer_class(self):
        if "search" in self.request.query_params:
            return CategoryWithProductSerializer  # Serializer with products field
        return CategorySerializer  # Default serializer without products


class FirmMVS(UserMixin, ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class ProductMVS(UserMixin, ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class PurchasesMVS(UserMixin, ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class SalesMVS(UserMixin, ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


class BrandMVS(UserMixin, ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
