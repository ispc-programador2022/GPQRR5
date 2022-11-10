from django.contrib import admin
from django.urls import path, include
from gestionScrapers.views import searchProducts, pruebas_script
import debug_toolbar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('busqueda_productos/', searchProducts),
    path('pruebas_script/',pruebas_script),
    path('__debug__/',include(debug_toolbar.urls))
]
