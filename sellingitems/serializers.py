from sellingitems.models import SellingItems
from rest_framework import serializers

class ItemsSerializers(serializers.ModelSerializer):
    class Meta:
        model=SellingItems
        fields='__all__'