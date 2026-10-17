from django.contrib import admin
from .models import Categoria, Vacante

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
list_display = ('nombre',)
search_fields = ('nombre',)

@admin.register(Vacante)
class VacanteAdmin(admin.ModelAdmin):
list_display = ('titulo', 'empresa', 'categoria', 'destacada', 'activa', 'fecha_publicacion')
list_filter = ('activa', 'destacada', 'categoria')
search_fields = ('titulo', 'empresa__nombre')
list_editable = ('destacada', 'activa')
