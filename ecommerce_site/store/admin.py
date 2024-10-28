from django.contrib import admin
from .models import Product, Order
from django.core.exceptions import ValidationError

# Register your models here.

class OrderInline(admin.TabularInline):
    model = Order  # The model to be edited inline
    extra = 1  # How many empty forms to display

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'stock', 'created_at', 'updated_at')
    search_fields = ('name',)
    list_filter = ('created_at',)
    inlines = [OrderInline]  # Enable inline editing for orders

class OrderAdmin(admin.ModelAdmin):
    list_display = ('product', 'quantity', 'total_price', 'created_at')
    search_fields = ('product__name',)
    list_filter = ('created_at',)

    def save_model(self, request, obj, form, change):
        # Validate stock before saving
        if obj.quantity > obj.product.stock:
            raise ValidationError("Not enough stock available for this product.")
        super().save_model(request, obj, form, change)

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)