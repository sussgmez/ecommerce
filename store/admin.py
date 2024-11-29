from django.contrib import admin
from .models import Product, ProductImage, Order, Category


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]


@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    pass