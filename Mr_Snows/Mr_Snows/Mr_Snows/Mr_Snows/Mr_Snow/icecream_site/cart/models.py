from django.db import models
from django.contrib.auth.models import User


class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product_id = models.IntegerField()
    product_name = models.CharField(max_length=200)
    price = models.FloatField()
    quantity = models.IntegerField(default=1)

    def __str__(self):
        return self.product_name


