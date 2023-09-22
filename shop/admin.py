from django.contrib import admin
from .models import *

class CustomerAdmin(admin.ModelAdmin):
    pass

class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'product_name', 'category', 'brand', 'price']

class ShopCartAdmin(admin.ModelAdmin):
    list_display = ['user', 'product', 'qty', 'price', 'amount']

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(Brand)
admin.site.register(ShopCart, ShopCartAdmin)
admin.site.register(Order)
admin.site.register(OrderProduct)
admin.site.register(Review)
admin.site.register(Wishlist)