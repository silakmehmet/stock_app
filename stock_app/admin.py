from django.contrib import admin

from .models import Category, Firm, Product, Purchases, Sales, Brand


class PurchasesAdmin(admin.ModelAdmin):
    exclude = ['price_total']


class SalesAdmin(admin.ModelAdmin):
    exclude = ['price_total']


admin.site.register(Category)
admin.site.register(Firm)
admin.site.register(Product)
admin.site.register(Purchases, PurchasesAdmin)
admin.site.register(Sales, SalesAdmin)
admin.site.register(Brand)
