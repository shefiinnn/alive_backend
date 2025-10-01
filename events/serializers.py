from rest_framework import serializers
from .models import Category, Product, GalleryImage, Enquiry, Order

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)

    class Meta:
        model = Product
        fields = ['id', 'name', 'description', 'price', 'category', 'image','category_name']

class GalleryImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = GalleryImage
        fields = ['id', 'image', 'description']

class EnquirySerializer(serializers.ModelSerializer):
    class Meta:
        model = Enquiry
        fields = ['id', 'name', 'email', 'message', 'replied', 'recieved_at','number']

class OrderSerializer(serializers.ModelSerializer):
    product_name = serializers.CharField(source='product.name', read_only=True)
    product_price=serializers.CharField(source='product.price',read_only=True)
    class Meta:
        model = Order
        fields = ['id', 'product','quantity', 'customer_name', 'date', 'status','product_name','product_price','address','number','place','email','price','subtotal']
    def create(self, validated_data):
        product = validated_data['product']
        validated_data['price'] = product.price
        validated_data['subtotal'] = product.price * validated_data.get('quantity', 1)
        return super().create(validated_data)
