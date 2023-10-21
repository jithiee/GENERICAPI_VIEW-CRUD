
from rest_framework import serializers
from api . models import Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Product
        fields  =[
            
            'title',
            'content',
            'price',
            
        ]
    
    # def create(self, validated_data):
    #     return super().create(validated_data)

       
