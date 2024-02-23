from rest_framework import serializers

from shops.models import Shop


class shopsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shop
        fields = '__all__'