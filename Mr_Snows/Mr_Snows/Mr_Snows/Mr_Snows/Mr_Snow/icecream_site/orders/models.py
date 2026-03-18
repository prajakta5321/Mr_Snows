from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class Order(models.Model):
    user = models.ForeignKey(User, null=True, blank=True, on_delete=models.SET_NULL)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)

    quantity = models.PositiveIntegerField()
    price = models.FloatField()
    total_amount = models.FloatField()

    customer_name = models.CharField(max_length=100, blank=True)
    phone = models.CharField(max_length=15, blank=True)
    address = models.TextField(blank=True)

    ordered_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        if self.user:
            return f"Order {self.id} - {self.user.username}"
        return f"Order {self.id}"