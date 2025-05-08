from django.contrib import admin
from .models import (
    Product, ProductType, SkinConcern, SkinType,
    Wishlist, Cart, CartItem,
    Order, OrderItem
)

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'is_in_stock')
    search_fields = ('name', 'description')
    list_filter = ('product_types', 'skin_concerns', 'skin_types')

class WishlistAdmin(admin.ModelAdmin):
    list_display = ('user',)
    filter_horizontal = ('products',)

class CartAdmin(admin.ModelAdmin):
    list_display = ('user',)

class CartItemAdmin(admin.ModelAdmin):
    list_display = ('cart', 'product', 'quantity', 'price')

class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'total_amount', 'status', 'created_at')
    list_filter = ('status', 'created_at')
    search_fields = ('user__username', 'shipping_name', 'shipping_address')

class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('order', 'product', 'quantity', 'price')

admin.site.register(Product, ProductAdmin)
admin.site.register(ProductType)
admin.site.register(SkinConcern)
admin.site.register(SkinType)
admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Cart, CartAdmin)
admin.site.register(CartItem, CartItemAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(OrderItem, OrderItemAdmin)

