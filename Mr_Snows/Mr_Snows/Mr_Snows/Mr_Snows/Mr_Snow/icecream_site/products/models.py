from django.db import models


class Product(models.Model):

    CATEGORY = (
        ('Scoop', 'Scoop'),
        ('Cone', 'Cone'),
        ('Cup', 'Cup'),
        ('Family Pack', 'Family Pack'),
    )

    name = models.CharField(max_length=100)
    price = models.IntegerField()
    type = models.CharField(max_length=50, choices=CATEGORY)
    flavour = models.CharField(max_length=100)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/')

    def __str__(self):
        return self.name

    # Fix for Djongo delete error
    def __hash__(self):
        return hash(self.pk)


class Order(models.Model):

    ORDER_TYPE = (
        ('DELIVERY', 'Delivery'),
        ('PICKUP', 'Pickup'),
    )

    customer_name = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=15)
    total_amount = models.FloatField()
    order_type = models.CharField(max_length=20, choices=ORDER_TYPE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order {self.id} - {self.customer_name}"