from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=200)
    weight = models.IntegerField()
    price = models.IntegerField()
    created_at = models.DateTimeField(blank=True, null=True)
    updated_at = models.DateTimeField(blank=True,null=True)


