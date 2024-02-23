from django.db import models
from shops.models import Shop
# Create your models here.
#billing information model
class BillingInfo(models.Model):
    customer_name = models.CharField(max_length=100)
    customer_address = models.CharField(max_length=100)
    customer_contact = models.CharField(max_length=100)
    customer_email = models.CharField(max_length=100)
    customer_gst = models.CharField(max_length=100)
    customer_items = models.ForeignKey('cart.CartModels',on_delete=models.PROTECT)
    customer_quantity = models.CharField(max_length=100)
    def __str__(self):
        return self.customer_name