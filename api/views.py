from django.shortcuts import render
from django.http import JsonResponse ,HttpResponse
from . models import Product
from django.forms.models import model_to_dict
import json
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ProductSerializer
# Create your views here.
@api_view(["POST"])
def api_home(request,*args,**kwargs):
    instance = Product.objects.all().order_by('?').first()
    data = {}
    if instance:
        # data['id'] = model_data.id
        # data['title'] = model_data.title
        # data['content'] = model_data.title
        # data['price'] = model_data.price
        # data = model_to_dict(model_data,fields=['id','title','price'])
        # json_data = json.dumps(data)
        data = ProductSerializer(instance).data
        
    # return HttpResponse (json_data, headers={"content-type":"application/json"})
    return Response(data)

        
    
