from django.urls import path
from . import views

urlpatterns = [
    path("", views.inicio, name="inicio"),
    # Crud Categorias
    path("categorias_listar/", views.categorias, name="categorias_listar"),
    path("categorias_form/", views.categorias_form, name="categorias_form"),
    path("categorias_crear/", views.categorias_crear, name="categorias_crear"),
    path("categorias_eliminar/<int:id>/", views.categorias_eliminar, name="categorias_eliminar"),
    path("categorias_form_editar/<int:id>/", views.categorias_form_editar, name="categorias_form_editar"),
    path("categorias_actualizar/", views.categorias_actualizar, name="categorias_actualizar"),
    # Crud Productos
    path("productos_listar/", views.productos, name="productos_listar"),
    path("productos_form/", views.productos_form, name="productos_form"),
    path("productos_crear/", views.productos_crear, name="productos_crear"),
    path("productos_eliminar/<int:id>/", views.productos_eliminar, name="productos_eliminar"),
    path("productos_form_editar/<int:id>/", views.productos_form_editar, name="productos_form_editar"),
    path("productos_actualizar/", views.productos_actualizar, name="productos_actualizar"),
    # Crud Usuarios
    path("usuarios_listar/", views.usuarios, name="usuarios_listar"),
    path("usuarios_form/", views.usuarios_form, name="usuarios_form"),
    path("usuarios_crear/", views.usuarios_crear, name="usuarios_crear"),
    path("usuarios_eliminar/<int:id>/", views.usuarios_eliminar, name="usuarios_eliminar"),
    path("usuarios_form_editar/<int:id>/", views.usuarios_form_editar, name="usuarios_form_editar"),
    path("usuarios_actualizar/", views.usuarios_actualizar, name="usuarios_actualizar"),
]
