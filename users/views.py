from django.shortcuts import render

# Create your views here.

from rest_framework.views import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated

from users.models import *
from users.serializers import *


class GetStudentsView(APIView):

    def get(self,request):
        print("req",request.GET)
        name = request.GET.get("myname")
        print("name",name)
        if name:
            instance = Students.objects.filter(first_name = name)
        else:
          instance = Students.objects.all()
        serializer = StudentsSerializers(instance,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        
        params = request.data
        print("params",params)

        serializer = StudentsSerializers(data=params)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"messege","Done"})
    
class GetOrdersViews(APIView):
    def get(self,request):
        print("req",request.GET)
        name = request.GET.get("myname")
        print("name",name)
        if name:
            instance = Orders.objects.filter(order_name = name)
        else:
          instance = Orders.objects.all()
        serializer = OrdersSerializers(instance,many=True)
        return Response(serializer.data)
    
    def post(self,request):
        
        params = request.data
        print("params",params)

        serializer = OrdersSerializers(data=params)
        serializer.is_valid(raise_exception=True)
        serializer.save()

        return Response({"messege","Done"})
    
class DeleteStudentsView(APIView):
    def get(self,request,pk):
        instance = Students.objects.get(id=pk)
        instance.delete()
        
        return Response({"messege","delete"}) 
    
class StudentsDetailsAddressViews(APIView):
    def get(self,request,pk):
        instance = Students.objects.filter(id=pk)
        serializer = StudentsDetailsAddressSerializers(instance,many=True)
        
        return Response(serializer.data) 
    

    

