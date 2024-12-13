from django.shortcuts import render, redirect
from .models import RegistroDeArchivo
from .forms import RegistroDeArchivoForm
from django.http import JsonResponse
from .models import SubserieDocumental
from .models import SerieDocumental
from django.contrib.auth.decorators import login_required

# from .models import SerieDocumental

# print(SerieDocumental)

@login_required
def cargar_series(request):
    series = SerieDocumental.objects.all().values('codigo', 'nombre')
    return JsonResponse(list(series), safe=False)
@login_required
def cargar_subseries(request):
    serie_id = request.GET.get('serie_id')  # esto será el id (entero)
    subseries = SubserieDocumental.objects.filter(serie_id=serie_id).values('id', 'nombre')
    return JsonResponse(list(subseries), safe=False)



@login_required
# Listar registros
def lista_registros(request):
    registros = RegistroDeArchivo.objects.all()
    return render(request, 'registro_list.html', {'registros': registros})

@login_required
def crear_registro(request):
    print("Vista 'crear_registro' ejecutándose...")  # Confirmación de ejecución
    if request.method == 'POST':
        print("Datos POST enviados:", request.POST)  # Imprime los datos enviados en el formulario

        form = RegistroDeArchivoForm(request.POST)
        if form.is_valid():
            print("Formulario válido")
            registro = form.save(commit=False)  # Crea el registro sin guardarlo todavía
            registro.creado_por = request.user  # Asigna el usuario autenticado al campo creado_por
            registro.save()  # Guarda el registro con el usuario asignado
            return redirect('lista_registros')
        else:
            print("Errores del formulario:", form.errors)  # Muestra los errores de validación

    else:
        print("Método GET recibido")
        form = RegistroDeArchivoForm()
        form.fields['codigo_subserie'].queryset = SubserieDocumental.objects.none()

    return render(request, 'registro_form.html', {'form': form})







def editar_registro(request, pk):
    registro = RegistroDeArchivo.objects.get(id=pk)
    if request.method == 'POST':
        form = RegistroDeArchivoForm(request.POST, instance=registro)
        
        # Recuperar el valor de la serie seleccionada para actualizar las subseries
        codigo_serie = request.POST.get('codigo_serie')
        if codigo_serie:
            form.fields['codigo_subserie'].queryset = SubserieDocumental.objects.filter(serie_id=codigo_serie)
        
        if form.is_valid():
            form.save()
            return redirect('lista_registros')
    else:
        form = RegistroDeArchivoForm(instance=registro)
        # Establecer el queryset de subseries basándose en la serie ya asociada al registro
        if registro.codigo_serie:
            form.fields['codigo_subserie'].queryset = SubserieDocumental.objects.filter(serie=registro.codigo_serie)
        else:
            form.fields['codigo_subserie'].queryset = SubserieDocumental.objects.none()




    return render(request, 'registro_form.html', {'form': form})


@login_required
def eliminar_registro(request, pk):
    registro = RegistroDeArchivo.objects.get(id=pk)
    if registro.creado_por != request.user:
        return HttpResponseForbidden("No tienes permiso para eliminar este registro.")
    registro.delete()
    return redirect('lista_registros')

@login_required
def lista_completa_registros(request):
    registros = RegistroDeArchivo.objects.all()
    return render(request, 'registro_completo.html', {'registros': registros})



