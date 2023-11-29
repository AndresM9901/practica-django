from django.contrib import admin
from .models import *

# Register your models here.
@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'descripcion']
    search_fields = ['nombre']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'precio', 'inventario', 'categoria']
    search_fields = ['nombre']
    list_editable = ['nombre', 'precio', 'inventario']
    list_filter = ['categoria', 'fecha_creacion']

@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    list_display = ['id', 'nombre', 'correo', 'contrasena', 'rol', 'foto']
