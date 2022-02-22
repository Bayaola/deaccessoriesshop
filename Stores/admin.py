from django import forms
from django.contrib import admin
from mptt.admin import MPTTModelAdmin

from .models import (
    Category,
    Product,
    ProductImage,
    ProductSpecification,
    ProductSpecificationValue,
    ProductType,
    CommentProduct
)

admin.site.register(Category, MPTTModelAdmin)

admin.site.register(ProductType)

admin.site.register(CommentProduct)


class ProductImageInline(admin.TabularInline):
    model = ProductImage



@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductImageInline,
    ]