from django.shortcuts import render
from rest_framework import generics
from .models import Tag
from .serializers import TagSerializer
from .models import Category
from .serializers import CategorySerializer


class TagListCreateView(generics.ListCreateAPIView):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CategoryListCreate(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer