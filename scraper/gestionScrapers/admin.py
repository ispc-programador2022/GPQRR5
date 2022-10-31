from unicodedata import category
from django.contrib import admin
from gestionScrapers.models import Venex

# Register your models here.
class VenexAdmin(admin.ModelAdmin):
    list_display = ('name', 'category', 'brand', 'price')
    search_fields = ('name', 'price')

admin.site.register(Venex, VenexAdmin)