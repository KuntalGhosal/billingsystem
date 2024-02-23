from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from shops.models import Shop
from shops.serializers import shopsSerializer
# Create your views here.

class ShopView(APIView):
    def get(self, request, *args, **kwargs):
        shoplist=[]
        if kwargs.get('id'):
            shoplist = Shop.objects.filter(id=kwargs.get('id'))
        elif kwargs.get('name'):
            shoplist = Shop.objects.filter(shop_name__icontains=kwargs.get('name'))
        else:
            print("goingg")
            shoplist = Shop.objects.all()
        return Response({'shopList':shopsSerializer(shoplist,many=True).data})
    
    def post(self, request, *args, **kwargs):
        shopList= shopsSerializer(data=request.data)
        if shopList.is_valid():
            shopList.save()
            return Response({'message':'Shop added successfully'})
        else:
            return Response(shopList.errors)
        
    def put(self, request, *args, **kwargs):
        shopList = Shop.objects.get(id=kwargs.get('id'))
        serializer = shopsSerializer(shopList, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Shop updated successfully'})
        else:
            return Response(serializer.errors)
        
    def delete(self, request, *args, **kwargs):
        shopList = Shop.objects.get(id=kwargs.get('id'))
        shopList.delete()
        return Response({'message':'Shop deleted successfully'})
            
         
