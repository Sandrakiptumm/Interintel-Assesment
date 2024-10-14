# models.py
from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    image = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ProductVariant(models.Model):
    product = models.ForeignKey(Product, related_name='variants', on_delete=models.CASCADE)
    sku = models.CharField(max_length=100)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    details = models.TextField(null=True, blank=True)

    def __str__(self):
        return f"{self.name} ({self.sku})"
