from rest_framework import viewsets
from .models import Category,Enquiry,GalleryImage,Order,Product
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.permissions import AllowAny
from .serializers import(CategorySerializer,GalleryImageSerializer,OrderSerializer,ProductSerializer,EnquirySerializer)

class CategoryViewSet(viewsets.ModelViewSet):
    queryset=Category.objects.all()
    serializer_class=CategorySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all()
    serializer_class=ProductSerializer

class GalleryImageViewSet(viewsets.ModelViewSet):
    queryset=GalleryImage.objects.all()
    serializer_class=GalleryImageSerializer
    parser_classes = [MultiPartParser, FormParser] 
    permission_classes = [AllowAny]

class OrderViewSet(viewsets.ModelViewSet):
    queryset=Order.objects.all()
    serializer_class=OrderSerializer

class EnquiryViewSet(viewsets.ModelViewSet):
    queryset=Enquiry.objects.all()
    serializer_class=EnquirySerializer
