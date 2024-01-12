# serializers.py
from rest_framework import serializers
from store.models import Product,Category,OrderItem


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):

    #call category in Product Serializer
    category=CategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'