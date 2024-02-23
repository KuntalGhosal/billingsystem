from billingInfo.models import BillingInfo
from rest_framework import serializers


class BillingInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = BillingInfo
        fields = '__all__'