from django.urls import path
from .views import CategoryListCreate, TagListCreateView  

urlpatterns = [
    path('tags/', TagListCreateView.as_view(), name='tag-list-create'),  
    path('categories/', CategoryListCreate.as_view(), name='category-list-create'), 
]
