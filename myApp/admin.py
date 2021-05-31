from django.contrib import admin
from .models.product import Product
from .models.category import Category

#Set list_display to control which fields are displayed on the change list page of the admin.
class AdminProduct(admin.ModelAdmin):
    list_display = ['name','price','category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']     

# Register your models here.

admin.site.register(Product,AdminProduct)
admin.site.register(Category,AdminCategory)
