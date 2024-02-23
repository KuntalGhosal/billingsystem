from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response

from cart.models import CartModels
from cart.serializers import CartSerializer

# Create your views here.
class CartView(APIView):
    def get(self,request,*args,**kwargs):
        cartList = CartModels.objects.all()
        return Response({'cart_list':CartSerializer(cartList,many=True).data})
    
    def post(self,request,*args,**kwargs):
        cartItem=CartSerializer(data=request.data)
        if cartItem.is_valid():
            cartItem.save()
            return Response({'cart_item':cartItem.data})
        else:
            return Response(cartItem.errors)
        
    def put(self,request,*args,**kwargs):
        cartItem = CartModels.objects.get(id=kwargs.get('id'))
        cartItemCheck = CartSerializer(cartItem,data=request.data)
        if cartItemCheck.is_valid():
            cartItemCheck.save()
            return Response({'message':'Cart item updated successfully'})
        else:
            return Response(cartItemCheck.errors)
        
    def delete(self,request,*args,**kwargs):
        cartItem = CartModels.objects.get(id=kwargs.get('id'))
        cartItem.delete()
        return Response({'message':'Cart item deleted successfully'})
        
        
    