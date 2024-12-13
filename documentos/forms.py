from django import forms
from .models import RegistroDeArchivo, SerieDocumental, SubserieDocumental
from django.utils.timezone import now
from django.forms import DateInput

class RegistroDeArchivoForm(forms.ModelForm):
    codigo_serie = forms.ModelChoiceField(
        queryset=SerieDocumental.objects.all(),
        empty_label="Seleccione una serie"
    )
    codigo_subserie = forms.ModelChoiceField(
        queryset=SubserieDocumental.objects.none(),
        empty_label="Seleccione una subserie"
    )

    # Hacemos opcionales los campos en el formulario
    caja = forms.CharField(required=False)
    carpeta = forms.CharField(required=False)
    tomo_legajo_libro = forms.CharField(required=False)
    numero_folios = forms.IntegerField(required=False)
    tipo = forms.CharField(required=False)
    cantidad = forms.IntegerField(required=False)
    ubicacion = forms.CharField(required=False)
    cantidad_documentos_electronicos = forms.IntegerField(required=False)
    tamano_documentos_electronicos = forms.CharField(required=False)

    class Meta:
        model = RegistroDeArchivo
        # Excluimos explícitamente el campo 'creado_por'
        exclude = ['creado_por']
        widgets = {
            'fecha_archivo': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_inicial': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'fecha_final': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if not self.instance.pk:  # Si es un nuevo registro
            self.fields['fecha_archivo'].initial = now().date()

        # Configuración dinámica del queryset de subseries
        if 'codigo_serie' in self.data:
            try:
                serie_id = int(self.data.get('codigo_serie'))
                self.fields['codigo_subserie'].queryset = SubserieDocumental.objects.filter(serie_id=serie_id)
            except (ValueError, TypeError):
                self.fields['codigo_subserie'].queryset = SubserieDocumental.objects.none()
        elif self.instance.pk and self.instance.codigo_serie:
            self.fields['codigo_subserie'].queryset = SubserieDocumental.objects.filter(serie_id=self.instance.codigo_serie.id)
        else:
            self.fields['codigo_subserie'].queryset = SubserieDocumental.objects.none()

    def clean(self):
        cleaned_data = super().clean()
        soporte_fisico = cleaned_data.get('soporte_fisico')
        soporte_electronico = cleaned_data.get('soporte_electronico')

        # Si soporte físico no está seleccionado, asignar valores predeterminados
        if not soporte_fisico:
            cleaned_data['caja'] = "N/A"
            cleaned_data['carpeta'] = "N/A"
            cleaned_data['tomo_legajo_libro'] = "N/A"
            cleaned_data['numero_folios'] = 0
            cleaned_data['tipo'] = "N/A"
            cleaned_data['cantidad'] = 0

        # Si soporte electrónico no está seleccionado, asignar valores predeterminados
        if not soporte_electronico:
            cleaned_data['ubicacion'] = "N/A"
            cleaned_data['cantidad_documentos_electronicos'] = 0
            cleaned_data['tamano_documentos_electronicos'] = "N/A"

        return cleaned_data



# hasta aca servia a las 4 `pm martes 10....................................................`
# class RegistroDeArchivoForm(forms.ModelForm):
#     codigo_serie = forms.ModelChoiceField(
#         queryset=SerieDocumental.objects.all(),
#         empty_label="Seleccione una serie"
#     )
#     codigo_subserie = forms.ModelChoiceField(
#         queryset=SubserieDocumental.objects.none(),
#         empty_label="Seleccione una subserie"
#     )

#     class Meta:
#         model = RegistroDeArchivo
#         fields = '__all__'
# .............................................................................................



# from django import forms
# from .models import RegistroDeArchivo, SubserieDocumental, SerieDocumental

# class RegistroDeArchivoForm(forms.ModelForm):
#     class Meta:
#         model = RegistroDeArchivo
#         fields = '__all__'

#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#         self.fields['codigo_serie'].queryset = SerieDocumental.objects.all()
#         self.fields['codigo_subserie'].queryset = SubserieDocumental.objects.none()

#         if 'codigo_serie' in self.data:
#             try:
#                 serie_id = int(self.data.get('codigo_serie'))
#                 self.fields['codigo_subserie'].queryset = SubserieDocumental.objects.filter(serie_id=serie_id)
#             except (ValueError, TypeError):
#                 pass
#         elif self.instance.pk:
#             self.fields['codigo_subserie'].queryset = SubserieDocumental.objects.filter(serie=self.instance.codigo_serie)
