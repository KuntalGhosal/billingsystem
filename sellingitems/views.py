from django.shortcuts import render
from rest_framework.views import APIView
from sellingitems.models import SellingItems
from rest_framework.response import Response
from sellingitems.serializers import ItemsSerializers

# Create your views here.

class SellingItemsView(APIView):
    def get(self,request,*args,**kwargs):
        itemList=[]
        if(kwargs.get('id')):
            itemList = SellingItems.objects.filter(shop_id=kwargs.get('id'))
        else:
            itemList = SellingItems.objects.all()
        return Response({'item_list':ItemsSerializers(itemList,many=True).data})
    
    def post(self,request,*args,**kwargs):
        itemList = ItemsSerializers(data=request.data)
        if itemList.is_valid():
            itemList.save()
            print(itemList)
            return Response({'item':itemList.data})
        else:
            return Response(itemList.errors)
        
    def put(self,request,*args,**kwargs):
        itemList = SellingItems.objects.get(id=kwargs.get('id'))
        serializer = ItemsSerializers(itemList,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Item updated successfully'})
        else:
            return Response(serializer.errors)
        
    def delete(self,request,*args,**kwargs):
        itemList = SellingItems.objects.get(id=kwargs.get('id'))
        itemList.delete()
        return Response({'message':'Item deleted successfully'})
    
