from unicodedata import category
from django.contrib import admin
from gestionScrapers.models import Product

# Register your models here.
'''
class VenexAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'price')
class FullHardAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'price')
class CompGamerAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'price')
class MeliAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'price')

admin.site.register(Venex, VenexAdmin)
admin.site.register(FullHard, FullHardAdmin)
admin.site.register(CompGamer, CompGamerAdmin)
admin.site.register(Meli, FullHardAdmin)
'''

class ProductAdmin(admin.ModelAdmin):
    list_display = ('page', 'title','price','brand','link','dateFormat')
    search_fields = ('page', 'title','price','brand','link','dateFormat')

admin.site.register(Product, ProductAdmin)