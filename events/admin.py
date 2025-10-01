from django.contrib import admin
from .models import Product, Category, Order, Enquiry, GalleryImage

admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Enquiry)
admin.site.register(GalleryImage)
