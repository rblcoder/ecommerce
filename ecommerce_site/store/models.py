from django.db import models
from django.core.exceptions import ValidationError

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    stock = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class Order(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total_price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.product.name}"

    def save(self, *args, **kwargs):
        # Ensure that the product has enough stock before creating the order
        if self.quantity > self.product.stock:
            raise ValidationError("Not enough stock available for this product.")
        
        # Call the original save method to save the order
        super().save(*args, **kwargs)
        
        # Decrease the stock of the product
        self.product.stock -= self.quantity
        self.product.save()