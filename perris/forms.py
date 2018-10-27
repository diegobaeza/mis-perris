from django import forms
from django.utils.translation import ugettext_lazy
from django.core.exceptions import ValidationError
from .models import *
import datetime



class RegistroForm(forms.ModelForm):
	
	contrasena = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
	region = forms.ModelChoiceField( queryset=Region.objects.all(), empty_label='Seleccione una Region', label='')
	class Meta:
		model = Usuario
		fields = ('run', 'nombre', 'apellido', 'fechaNacimiento', 'telefono', 'correo', 'region', 'ciudad', 'tipoVivienda', 'contrasena')

		labels = {
			'run' : 'Run',
			'nombre' : 'Nombre',
			'apellido' : 'Apellido',
			'fechaNacimiento' : 'Fecha de Nacimiento',
			'telefono' : 'Telefono',
			'correo' : 'Correo',
			'tipoVivienda' : 'Tipo de Vivienda'
			}

