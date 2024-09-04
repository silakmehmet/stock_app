from django.db import models
from django.contrib.auth.models import User


class Firm(models.Model):
    name = models.CharField(max_length=150, unique=True)
    phone = models.CharField(max_length=60, unique=True)
    address = models.CharField(max_length=255, unique=True)
    image = models.TextField(null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=60, unique=True)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name


class Brand(models.Model):
    name = models.CharField(max_length=60)
    image = models.TextField(null=True, blank=True)
    category = models.ManyToManyField(Category, related_name="brand_category")
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        categories = ", ".join([cat.name for cat in self.category.all()])
        return f"{self.name} - {categories}"


class Product(models.Model):
    name = models.CharField(max_length=100)
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="product_category")
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name="product_brand")
    stock = models.PositiveSmallIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} - {self.brand}"


class Purchases(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="purchase_user")
    firm = models.ForeignKey(
        Firm, on_delete=models.CASCADE, related_name="purchase_firm")
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name="purchase_brand")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="purchase_product")
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_total = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Purchase"
        verbose_name_plural = "Purchases"

    def save(self, *args, **kwargs):
        self.price_total = self.quantity * self.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} - {self.quantity} pcs'


class Sales(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="sale_user")
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="sale_product")
    brand = models.ForeignKey(
        Brand, on_delete=models.CASCADE, related_name="sale_brand")
    quantity = models.PositiveSmallIntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    price_total = models.DecimalField(max_digits=10, decimal_places=2)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = "Sale"
        verbose_name_plural = "Sales"

    def save(self, *args, **kwargs):
        self.price_total = self.quantity * self.price
        super().save(*args, **kwargs)

    def __str__(self):
        return f'{self.product.name} - {self.quantity} pcs'
