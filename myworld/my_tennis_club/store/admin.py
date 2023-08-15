from django.contrib import admin
from .import models
from .models import Product


#@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
      list_display = ['title', 'unit_price']                
                      
admin.site.register(models.Collection)
# Register your models here.

admin.site.register(models.Product, ProductAdmin)
