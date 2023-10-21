from rest_framework import serializers
from .models import Product
from rest_framework import generics,views,viewsets 

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields  =[
            'title',
            'content',
            'price',
            
        ]
        
    def validator(self,data):
        data = data.get('title',)
  
       
