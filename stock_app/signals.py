from django.db.models.signals import post_save, post_delete, pre_save
from django.dispatch import receiver

from .models import Purchases, Sales


# Capturing old instance before update
@receiver(pre_save, sender=Purchases)
def capture_old_quantity_purchase(sender, instance, **kwargs):
    if instance.id:
        old_instance = Purchases.objects.get(id=instance.id)
        instance._old_quantity = old_instance.quantity
    else:
        instance._old_quantity = 0  # This is a new instance


@receiver(pre_save, sender=Sales)
def capture_old_quantity_sale(sender, instance, **kwargs):
    if instance.id:
        old_instance = Sales.objects.get(id=instance.id)
        instance._old_quantity = old_instance.quantity
    else:
        instance._old_quantity = 0  # This is a new instance


@receiver(post_save, sender=Purchases)
def update_stock_after_purchase(sender, instance, created, **kwargs):
    if created:
        # Increasing stock with new purchase
        product = instance.product
        product.stock += instance.quantity
        product.save()
    else:
        # Updating purchase, adjusting stock accordingly
        stock_change = instance.quantity - instance._old_quantity
        instance.product.stock += stock_change
        instance.product.save()


@receiver(post_save, sender=Sales)
def update_stock_after_sale(sender, instance, created, **kwargs):
    if created:
        # Decreasing stock with new sale
        product = instance.product
        product.stock -= instance.quantity
        product.save()
    else:
        # Updating sale, adjusting stock accordingly
        stock_change = instance._old_quantity - instance.quantity
        instance.product.stock += stock_change
        instance.product.save()


@receiver(post_delete, sender=Purchases)
def decrease_stock_after_purchase_delete(sender, instance, **kwargs):
    # Decreasing stock when a purchase is deleted
    product = instance.product
    product.stock -= instance.quantity
    product.save()


@receiver(post_delete, sender=Sales)
def increase_stock_after_sale_delete(sender, instance, **kwargs):
    # Increasing stock when a sale is deleted
    product = instance.product
    product.stock += instance.quantity
    product.save()
