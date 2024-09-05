from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.viewsets import ModelViewSet
from rest_framework.filters import SearchFilter, OrderingFilter

from .permissions import IsAuthenticatedOrReadOnly
from .models import Category, Firm, Product, Purchases, Sales, Brand
from .serializers import CategorySerializer, CategoryWithProductSerializer, FirmSerializer, ProductSerializer, PurchasesSerializer, SalesSerializer, BrandSerializer
from .mixins import UserMixin


class CategoryMVS(UserMixin, ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["name"]
    filterset_fields = ["name"]

    def get_serializer_class(self):
        if "search" in self.request.query_params:
            return CategoryWithProductSerializer  # Serializer with products field
        return CategorySerializer  # Default serializer without products


class FirmMVS(UserMixin, ModelViewSet):
    queryset = Firm.objects.all()
    serializer_class = FirmSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ["name"]


class ProductMVS(UserMixin, ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["name"]
    ordering_fields = ["category", "brand"]
    filterset_fields = ["category", "brand"]


class PurchasesMVS(UserMixin, ModelViewSet):
    queryset = Purchases.objects.all()
    serializer_class = PurchasesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["firm"]
    ordering_fields = ["firm", "product"]
    filterset_fields = ["firm", "product"]


class SalesMVS(UserMixin, ModelViewSet):
    queryset = Sales.objects.all()
    serializer_class = SalesSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    search_fields = ["brand"]
    ordering_fields = ["brand", "product"]
    filterset_fields = ["brand", "product"]


class BrandMVS(UserMixin, ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [SearchFilter]
    search_fields = ["name"]
