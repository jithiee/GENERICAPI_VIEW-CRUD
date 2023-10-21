from rest_framework import generics,mixins
from  api.models import Product
from  .serializers import ProductSerializer


# ======================  GENERICAPIVIEWS  ============================================================
#======================================================================================================

# Retrieve all datas and the specific product with id=1 get with clint url ===========================================================================

class ProductDetailsApiview(generics.RetrieveAPIView):
      queryset = Product.objects.all()  # Retrieve all products
      serializer_class = ProductSerializer
      
      # def get_object(self):
            
      #       return  Product.objects.get(id=1)   # Retrieve the specific product with id=1
      
#=======================================================================================================================   
   
# create new product (POST)==================================================================================================  

class ProductCreateApiview(generics.CreateAPIView):
      queryset = Product.objects.all()
      serializer_class = ProductSerializer
      
      def perform_create(self, serializer):   #serializer is instance of serializer_class we can use other name as a perameter
           
            print(serializer)
            title = serializer.validated_data.get('title')
            price = serializer.validated_data.get('price')
            content = serializer.validated_data.get('content')
            
            if content is None:
                  content = title
            serializer.save(content = content)
      
            
            
        

            
#==============================================================================================================            

# ListCreateAPIView is used for get and post 
class ProductListcreateApiviews(generics.ListCreateAPIView):
      queryset = Product.objects.all()
      serializer_class = ProductSerializer
      
      def list_create(self,serializer):
            serializer.validated_data.get('title')
            serializer.validated_data.get('content') 
            serializer.validated_data.get('price')
            serializer.save()
            

#============================================================================================================

class ProductUpdateApiview(generics.UpdateAPIView):
      queryset =Product.objects.all()
      serializer_class = ProductSerializer # there converting  happend
      lookup_field = 'pk'  
      
      
      def perform_update(self,serializer):
             serializer.save() #inctance means perform_create through created datas
            
#=============================================================================================     

class ProductDeleteApiview(generics.DestroyAPIView):
      queryset = Product.objects.all()
      serializer_class = ProductSerializer
      lookup_field = 'pk'
      
      def perform_destory(self,instance):
            #instance
            super().perform_destroy(instance)
            
#==================================================================================================
              # Mixins
              
# class ProductMixinView(mixins.ListModelMixin , generics.GenericAPIView):
      
#       queryset = Product.objects.all()
#       serializer_class = ProductSerializer
      
#       def get(self,request,*args, **kwargs):
#             return self.list(request,*args, **kwargs)  # the list method comming from  mixins.ListModelMixin   
                   
# Product_Mixin_View = ProductMixinView.as_view()            
            
# ==========================================================================================             
                     
                     
                     