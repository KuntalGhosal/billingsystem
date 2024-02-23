from django.shortcuts import render
from rest_framework.response import Response
from billingInfo.models import BillingInfo
from rest_framework.views import APIView
from billingInfo.serializers import BillingInfoSerializer

# Create your views here.

class BillingInfoView(APIView):
    def get(self, request, *args, **kwargs):
        billinglist=[]
        if kwargs.get('id'):
            billinglist = BillingInfo.objects.filter(shop_id=kwargs.get('id'))
        else:
            billinglist = BillingInfo.objects.all()
        return Response({'billingList':BillingInfoSerializer(billinglist,many=True).data})
    
    def post(self, request, *args, **kwargs):
        billingList= BillingInfoSerializer(data=request.data)
        if billingList.is_valid():
            billingList.save()
            return Response({'message':'Billing Info added successfully'})
        else:
            return Response(billingList.errors)
        
    def put(self, request, *args, **kwargs):
        billingList = BillingInfo.objects.get(id=kwargs.get('id'))
        serializer = BillingInfoSerializer(billingList, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Billing Info updated successfully'})
        else:
            return Response(serializer.errors)
        
    def delete(self, request, *args, **kwargs):
        billingList = BillingInfo.objects.get(id=kwargs.get('id'))
        billingList.delete()
        return Response({'message':'Billing Info deleted successfully'})
