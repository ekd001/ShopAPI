from django.shortcuts import render

from shop.models import Category,Product
from shop.serializers import CategorySerializer,ProductSerializer
from rest_framework.viewsets import ModelViewSet,ReadOnlyModelViewSet
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class ProductViewSet(ModelViewSet):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return Product.objects.all()


class CategoryViewSet(ReadOnlyModelViewSet):
    serializer_class = CategorySerializer
    def get_queryset(self):
        return Category.objects.all()


