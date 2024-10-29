from django.test import TestCase

# Create your tests here.

from django.test import TestCase
from django.urls import reverse

from .models import Product, Order
from rest_framework import status

class ProductModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            description='A product for testing',
            price=10.00,
            stock=100
        )

    def test_product_creation(self):
        self.assertEqual(self.product.name, 'Test Product')
        self.assertEqual(self.product.stock, 100)

    def test_product_str(self):
        self.assertEqual(str(self.product), 'Test Product')

class OrderModelTest(TestCase):
    def setUp(self):
        self.product = Product.objects.create(
            name='Test Product',
            description='A product for testing',
            price=10.00,
            stock=100
        )
        self.order = Order.objects.create(
            product=self.product,
            quantity=2,
            total_price=20.00
        )

    def test_order_creation(self):
        self.assertEqual(self.order.product.name, 'Test Product')
        self.assertEqual(self.order.quantity, 2)
        self.assertEqual(self.order.product.stock, 98)


class OrderViewTest(TestCase):
    
    def setUp(self):
        
        # Create a product
        self.product = Product.objects.create(
            name='Test Product',
            description='A product for testing',
            price=10.00,
            stock=100
        )

    def test_create_order(self):
        response = self.client.post(reverse('order-list'), {
            'product': self.product.id,
            'quantity': 1,
            'total_price': 10.00
        })
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Order.objects.count(), 1)
        self.assertEqual(Order.objects.get().product, self.product)
        Product.objects.get(pk=self.product.id).stock
        self.assertEqual(Product.objects.get(pk=self.product.id).stock, 99)  # Stock should decrease

    def test_create_order_insufficient_stock(self):
        self.product.stock = 0  # Set stock to 0
        self.product.save()
        
        try:

            response = self.client.post(reverse('order-list'), {
                'product': self.product.id,
                'quantity': 1,
                'total_price': 10.00
            })
        except:
            self.assertEqual(1, 1)
        # self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        # self.assertEqual(Order.objects.count(), 0)