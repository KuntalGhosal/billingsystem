from django.db import models

# Models for cart list
class CartModels(models.Model):
    added_items = models.ManyToManyField('sellingitems.SellingItems')
    date_added = models.DateTimeField(auto_now_add=True)
    total_cost = models.FloatField(default=0.0)
    shop_id = models.ForeignKey('shops.Shop',on_delete=models.PROTECT)
    

