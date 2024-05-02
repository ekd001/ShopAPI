from rest_framework.serializers import ModelSerializer
from rest_framework import serializers
from shop.models import Category,Product

class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','name','description','category','date_created','date_updated','active']
    


class CategorySerializer(ModelSerializer):
    products = serializers.SerializerMethodField()
    class Meta:
        model = Category
        fields = ['id','name','date_created','date_updated','description','products']

    def get_products(self,instance):
            queryset = instance.products.all()
            serializer = ProductSerializer(queryset,many=True)
            return serializer.data



