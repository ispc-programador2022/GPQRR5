from unicodedata import category
from django.contrib import admin
from gestionScrapers.models import Venex, FullHard

# Register your models here.
class VenexAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'price')
class FullHardAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    search_fields = ('name', 'price')

admin.site.register(Venex, VenexAdmin)
admin.site.register(FullHard, FullHardAdmin)