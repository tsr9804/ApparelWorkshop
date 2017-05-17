from __future__ import unicode_literals
from django.db import models
from jsonfield import JSONField

class Product(models.Model):
 
    asin = models.CharField(max_length=12, unique=True, null=False)
    title = models.TextField(null=False, default='')
    image = models.URLField(max_length=200, null=True)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=True)
    currency = models.CharField(max_length=100, null=False, default='')
    brand = models.CharField(max_length=100, null=True)
    model = models.CharField(max_length=100, null=True)
    manufacturer = models.CharField(max_length=100, null=True)
    features = JSONField()
    itemURL = models.TextField(null=False, default='')
    top_seller = models.BooleanField(default=True)
    category = models.TextField(max_length=40, null=True)
    editorial = models.TextField(null=True)
    editorial_short = models.TextField(null=True)

   
    #gathers top listings in our database, of the category requested (cat)
    def gather_top(self, cat):
        top = Product.objects.filter(top_seller=True, category = cat)
        return top       


