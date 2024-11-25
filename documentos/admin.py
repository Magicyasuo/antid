from django.contrib import admin
from .models import SerieDocumental, SubserieDocumental, RegistroDeArchivo, PermisoUsuarioSerie

@admin.register(SerieDocumental)
class SerieDocumentalAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre')
    search_fields = ('codigo', 'nombre')

@admin.register(SubserieDocumental)
class SubserieDocumentalAdmin(admin.ModelAdmin):
    list_display = ('codigo', 'nombre', 'serie')
    list_filter = ('serie',)
    search_fields = ('codigo', 'nombre')

@admin.register(RegistroDeArchivo)
class RegistroDeArchivoAdmin(admin.ModelAdmin):
    list_display = (
        'numero_orden', 'unidad_documental', 'fecha_archivo', 
        'creado_por', 'ubicacion', 'soporte_fisico', 'soporte_electronico'
    )
    list_filter = ('soporte_fisico', 'soporte_electronico', 'fecha_archivo', 'creado_por')
    search_fields = ('numero_orden', 'unidad_documental', 'ubicacion', 'notas')
    readonly_fields = ('fecha_creacion',)
    fieldsets = (
        ('Información General', {
            'fields': ('numero_orden', 'codigo_serie', 'codigo_subserie', 'unidad_documental','fecha_archivo', 
                        'fecha_inicial', 'fecha_final', 'notas')
        }),
        ('Soporte', {
            'fields': ('soporte_fisico', 'soporte_electronico', 'caja', 'carpeta', 
                       'tomo_legajo_libro', 'numero_folios', 'cantidad', 'ubicacion')
        }),
        ('Información Electrónica', {
            'fields': ('cantidad_documentos_electronicos', 'tamano_documentos_electronicos')
        }),
        ('Metadatos', {
            'fields': ('creado_por', 'fecha_creacion')
        }),
    )


