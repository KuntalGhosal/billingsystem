from django.db import models

# Create your models here.
#shop_name, shop_address, shop_contact, shop_email
class Shop(models.Model):
    shop_name = models.CharField(max_length=100)
    shop_address = models.CharField(max_length=100)
    shop_contact = models.CharField(max_length=100)
    shop_email = models.CharField(max_length=100)
    shop_gst = models.CharField(max_length=100)
    def __str__(self):
        return self.shop_name