from cart.models import CartModels
from rest_framework import serializers

class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = CartModels
        fields = '__all__'