from unicodedata import category
from django.contrib import admin
from gestionScrapers.models import Product

# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ('page', 'title','price','link')
    search_fields = ('page', 'title','price')

admin.site.register(Product, ProductAdmin)