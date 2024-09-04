from django.contrib import admin

from .models import Category, Firm, Product, Purchases, Sales, Brand


admin.site.register(Category)
admin.site.register(Firm)
admin.site.register(Product)
admin.site.register(Purchases)
admin.site.register(Sales)
admin.site.register(Brand)
