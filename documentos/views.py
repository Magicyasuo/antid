from django.shortcuts import render, redirect
from .models import RegistroDeArchivo
from .forms import RegistroDeArchivoForm

# Listar registros
def lista_registros(request):
    registros = RegistroDeArchivo.objects.all()
    return render(request, 'registro_list.html', {'registros': registros})

# Crear un nuevo registro
def crear_registro(request):
    if request.method == 'POST':
        form = RegistroDeArchivoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_registros')
    else:
        form = RegistroDeArchivoForm()
    return render(request, 'registro_form.html', {'form': form})

# Editar un registro existente
def editar_registro(request, pk):
    registro = RegistroDeArchivo.objects.get(id=pk)
    if request.method == 'POST':
        form = RegistroDeArchivoForm(request.POST, instance=registro)
        if form.is_valid():
            form.save()
            return redirect('lista_registros')
    else:
        form = RegistroDeArchivoForm(instance=registro)
    return render(request, 'registro_form.html', {'form': form})

# Eliminar un registro
def eliminar_registro(request, pk):
    registro = RegistroDeArchivo.objects.get(id=pk)
    registro.delete()
    return redirect('lista_registros')
