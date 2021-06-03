from django.db import models
from decimal import Decimal
# Create your models here.


class Product(models.Model):
    name = models.CharField(db_index=True, max_length=500)
    url = models.CharField(max_length=1000)
    website_name = models.CharField(max_length=20)
    image_url = models.CharField(blank=True, max_length=1000)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=Decimal(0.000))
    rating = models.DecimalField(decimal_places=1, null=True, max_digits=3)
    counter = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)