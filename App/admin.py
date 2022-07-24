from django.contrib import admin
from .models import *


# Register your models here.
class LocalesAdmin(admin.ModelAdmin):
    list_display = ("name","city","address","mall_number","opening_hours")
    search_fields = ("name","city","address","mall_number","opening_hours")
    
admin.site.register(Locales, LocalesAdmin) 


class VendedoresAdmin(admin.ModelAdmin):
    list_display = ("name","last_name","email","mall_number","birthday")
    search_fields = ("name","last_name","email","mall_number","birthday")
    
admin.site.register(Vendedores, VendedoresAdmin) 


class ProductosAdmin(admin.ModelAdmin):
    list_display = ("product","prize","brand","stock")
    search_fields = ("product","prize","brand","stock")
    
admin.site.register(Productos, ProductosAdmin) 


class NuevosProductosAdmin(admin.ModelAdmin):
    list_display = ("product","brand","release_date")
    search_fields = ("product","brand","release_date")
    
admin.site.register(Nuevos_Productos, NuevosProductosAdmin) 