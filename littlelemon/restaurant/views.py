from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView 

from .models import *
from .serializers import *
# from django.shortcuts import render

# Create your views here. 
class MenuItemsView(ListCreateAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

class SingleMenuItemView(RetrieveUpdateDestroyAPIView):
    queryset = MenuItem.objects.all()
    serializer_class = MenuItemSerializer

# Create your views here.
class BookingView(APIView):

    def get(self, request):
        items = Booking.objects.all()
        serializer = BookingSerializer(items, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = MenuItemSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response({"status":"success", "data":serializer.data})
        

# class MenuItemsView(ListCreateAPIView):

#     def get(self, request):
#         items = Menu.objects.all()
#         serializer = MenuItemSerializer(items, many=True)
#         return Response(serializer.data)
    
