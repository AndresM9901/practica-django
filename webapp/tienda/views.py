from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages

# Create your views here.
def inicio(request):
    return render(request,'tienda/inicio.html')

def categorias(request):
    q = Categoria.objects.all()
    context = {'data': q}
    return render(request,'tienda/categorias/categorias.html', context)

def categorias_form(request):
    return render(request, 'tienda/categorias/categorias_form.html')

def categorias_crear(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        try:
            q = Categoria(
                nombre = nombre,
                descripcion = descripcion
            )
            q.save()
            messages.success(request, f'Categoria guardada correctamente')
        except Exception as e:
            messages.error(request, f'Error: {e}')
        return redirect('categorias_listar')
    else:
        messages.warning(request, f'No se enviaron datos')
        return redirect('categorias_listar')

def categorias_eliminar(request, id):
    try:
        q = Categoria.objects.get(pk=id)
        q.delete()
        messages.success(request, f'Categoria eliminada correctamente')
    except Exception as e:
        messages.error(request, f'Error: {e}')
    return redirect('categorias_listar')

def categorias_form_editar(request, id):
    q = Categoria.objects.get(pk=id)
    context = {'data': q}
    return render(request, 'tienda/categorias/categorias_form_editar.html', context)

def categorias_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        descripcion = request.POST.get('descripcion')
        try:
            q = Categoria.objects.get(pk=id)
            q.nombre = nombre
            q.descripcion = descripcion
            q.save()
            messages.success(request, f'Categoria actualizada correctamente')
        except Exception as e:
            messages.error(request, f'Error: {e}')
        return redirect('categorias_listar')
    else:
        messages.warning(request, f'No se enviaron datos')
        return redirect('categorias_listar')
    
# Crud de Productos
def productos(request):
    q = Producto.objects.all()
    context = {'data': q}
    return render(request,'tienda/productos/productos.html', context)

def productos_form(request):
    q = Categoria.objects.all()
    contexto = {'data': q}
    return render(request, 'tienda/productos/productos_form.html', contexto)

def productos_crear(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        inventario = request.POST.get('inventario')
        fecha_creacion = request.POST.get('fecha_creacion')
        categoria = Categoria.objects.get(pk=request.POST.get('categoria'))
        try:
            q = Producto(
                nombre = nombre,
                precio = precio,
                inventario = inventario,
                fecha_creacion = fecha_creacion,
                categoria = categoria
            )
            q.save()
            messages.success(request, f'Producto guardado correctamente')
        except Exception as e:
            messages.error(request, f'Error: {e}')
        return redirect('productos_listar')
    else:
        messages.warning(request, f'No se enviaron datos')
        return redirect('productos_listar')
    
def productos_eliminar(request, id):
    try:
        q = Producto.objects.get(pk=id)
        q.delete()
        messages.success(request, f'Categoria eliminada correctamente')
    except Exception as e:
        messages.error(request, f'Error: {e}')
    return redirect('productos_listar')

def productos_form_editar(request, id):
    q = Producto.objects.get(pk=id)
    c = Categoria.objects.all()
    context = {'data': q, 'categoria': c}
    return render(request, 'tienda/productos/productos_form_editar.html', context)

def productos_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        precio = request.POST.get('precio')
        inventario = request.POST.get('inventario')
        fecha_creacion = request.POST.get('fecha_creacion')
        categoria = Categoria.objects.get(pk=request.POST.get('descripcion'))
        try:
            q = Producto.objects.get(pk=id)
            q.nombre = nombre
            q.precio = precio
            q.inventario = inventario
            q.fecha_creacion = fecha_creacion
            q.categoria = categoria
            q.save()
            messages.success(request, f'Producto actualizado correctamente')
        except Exception as e:
            messages.error(request, f'Error: {e}')
        return redirect('productos_listar')
    else:
        messages.warning(request, f'No se enviaron datos')
        return redirect('productos_listar')
    
# Crud Usuarios
def usuarios(request):
    q = Usuario.objects.all()
    contexto = {'data': q}
    return render(request, 'tienda/login/usuarios.html', contexto)

def usuarios_form(request):
    return render(request, 'tienda/login/usuarios_form.html')

def usuarios_crear(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        rol = request.POST.get("rol")
        foto = request.FILES.get('foto')
        try:
            q = Usuario(
                nombre=nombre,
                correo=correo,
                contrasena=contrasena,
                rol=rol,
                foto=foto,
            )
            q.save()
            messages.success(request, "Fue creado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')

        return redirect('usuarios_listar')
    else:
        messages.warning(request,'No se enviaron datos')
        return redirect('usuarios_listar')
    
def usuarios_eliminar(request, id):
    try:
        q = Usuario.objects.get(pk = id)
        q.delete()
        messages.success(request, 'Usuario eliminado correctamente!!')
    except Exception as e:
        messages.error(request,f'Error: {e}')

    return redirect('usuarios_listar')

def usuarios_form_editar(request, id):
    q = Usuario.objects.get(pk = id)
    contexto = {'data': q}

    return render(request, 'tienda/login/usuarios_form_editar.html', contexto)

def usuarios_actualizar(request):
    if request.method == 'POST':
        id = request.POST.get('id')
        nombre = request.POST.get('nombre')
        correo = request.POST.get('correo')
        contrasena = request.POST.get('contrasena')
        rol = request.POST.get('rol')
        foto = request.POST.get('foto')
        try:
            q = Usuario.objects.get(pk = id)
            q.nombre = nombre
            q.correo = correo
            q.contrasena = contrasena
            q.rol = rol
            q.foto = foto
            q.save()
            messages.success(request, "Fue actualizado correctamente")
        except Exception as e:
            messages.error(request,f'Error: {e}')
    else:
        messages.warning(request,'No se enviaron datos')

    return redirect('usuarios_listar')