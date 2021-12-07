from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import (
    Supplier,
    Buyer,
    Season,
    Product,
    
    
)

class SupplierAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'address', 'created_date']
    search_fields = ('name', 'address')
      

class BuyerAdmin(admin.ModelAdmin):
    list_display = [ 'name', 'address', 'created_date']
    search_fields = ('name', 'address')

class SeasonAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'created_date']
    search_fields = ('name', 'description')

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name', 'sortno', 'created_date']
    search_fields = ('name', 'sortno')
    


admin.site.register(Supplier, SupplierAdmin)
admin.site.register(Buyer, BuyerAdmin)
admin.site.register(Season, SeasonAdmin)
admin.site.register(Product, ProductAdmin)

