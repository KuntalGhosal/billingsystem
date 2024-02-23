from django.db import models

# Create modal for selling items for the shop

class SellingItems(models.Model):
    item_name = models.CharField(max_length=100)
    item_description = models.CharField(max_length=100)
    item_price = models.CharField(max_length=100)
    item_quantity = models.CharField(max_length=100)
    item_category = models.CharField(max_length=100)
    shop_id = models.ForeignKey('shops.Shop', on_delete=models.PROTECT)
    def __str__(self):
        return self.item_name
