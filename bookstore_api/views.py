from django.shortcuts import render

        
    
# from store.models import Product

# from rest_framework.views import APIView
# from rest_framework.response import Response
# class BookApiView(APIView):
#    def get(self,request):
#        allproduct = Product.objects.all().values()
#        return Response({"Message":"Available products","Book List":allproduct})
   
#    def post(self,request):
#        Product.objects.create(name = request.data["name"],
#                            author = request.data["author"],
#                            category = request.data["category"])
#        products = Product.objects.all().filter(name= request.data["name"]).values()
#        return Response({"Message":"New product","product":products})


# views.py
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import status
from store.models import Product, Category
from .serializers import ProductSerializer,CategorySerializer

from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


class BookApiView(generics.ListCreateAPIView):
    # authentication_classes = [TokenAuthentication]
    # permission_classes = [IsAuthenticated]
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

    def get(self, request, *args, **kwargs):
        products = self.get_queryset()
        serializer = self.serializer_class(products, many=True)
        return Response(serializer.data)
    



    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    


    def delete(self):
        try:
            products = self.get_queryset()
        except Product.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        products.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    