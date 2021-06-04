from django.db import models
from decimal import Decimal
# Create your models here.


class Product(models.Model):
    name = models.CharField(db_index=True, max_length=500)
    url = models.CharField(max_length=1000)
    website_name = models.CharField(max_length=20)
    image_url = models.CharField(blank=True, max_length=1000)
    price = models.CharField(max_length=20, default="0.00")
    rating = models.CharField(max_length=20, default="0.00", blank=True)
    counter = models.IntegerField(default=1)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)