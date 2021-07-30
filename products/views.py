from rest_framework.generics import ListAPIView
from rest_framework import permissions
from products.models import product
from .serializers import ProductSerializer
# Create your views here.
class ProductListView(ListAPIView):
    queryset = product.objects.all()
    serializer_class  = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
    #def get_queryset(): 
     
    