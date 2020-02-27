from django.contrib import admin

# Register your models here.
from .models import Product, ProductImage
from product.models import ProductImage, Category

admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(Category)
