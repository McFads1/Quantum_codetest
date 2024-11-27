from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics

from interview.order.models import Order, OrderTag
from interview.order.serializers import OrderSerializer, OrderTagSerializer

# Create your views here.
class OrderListCreateView(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    

class OrderTagListCreateView(generics.ListCreateAPIView):
    queryset = OrderTag.objects.all()
    serializer_class = OrderTagSerializer


class DeactivateOrderview(generics.UpdateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    def post(self, request, *args, **kwargs):
        order = self.get_object()
        if not order.is_active:
            return Response({'error': f'Order {order.id} is already deactivated'}, status=status.HTTP_400_BAD_REQUEST)
        
        order.is_active = False
        order.save()

        return Response({'message': f'Order {order.id} has been deactivated'}, status=status.HTTP_200_OK)