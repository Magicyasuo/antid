from django import forms
from .models import RegistroDeArchivo

class RegistroDeArchivoForm(forms.ModelForm):
    class Meta:
        model = RegistroDeArchivo
        fields = '__all__'
        widgets = {
            'numero_orden': forms.TextInput(attrs={'class': 'form-control'}),
            'fecha_archivo': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'notas': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
        }
