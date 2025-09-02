from django.contrib import admin
from .models import Category, Product, Order, OrderItem

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion')
    
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'descripcion', 'precio', 'categoria', 'imagen')

@admin.register(OrderItem)
class OrderItemAdmin(admin.ModelAdmin):
    list_display = ('pedido', 'producto', 'cantidad', 'precio_unitario')

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'fecha', 'estado', 'total')
