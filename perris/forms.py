from django import forms
from django.utils.translation import ugettext_lazy
from django.core.exceptions import ValidationError
from .models import *
import datetime
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User




class RegistroForm(forms.ModelForm):

	username = forms.CharField(label='Nombre de Usuario')
	password = forms.CharField(widget=forms.PasswordInput, label = 'Contraseña')
	password1 = forms.CharField(widget=forms.PasswordInput, label = 'Confirmar Contraseña')
	region = forms.ModelChoiceField(queryset=Region.objects.all(), empty_label="Seleccione una Region", label = "")
	ciudad = forms.ModelChoiceField(queryset=Ciudad.objects.all(), empty_label="Seleccione una Ciudad", label = "")
	tipoVivienda = forms.ModelChoiceField(queryset=TipoVivienda.objects.all(), empty_label="Seleccione su Tipo de Vivienda", label = "")
	
	def clean_password1(self):

	     cd = self.cleaned_data

	     password1 = cd.get('password')
	     password2 = cd.get('password1')

	     if password1 != password2:
	          raise ValidationError("Las contraseñas no coinciden")

	     return cd

	class Meta:
		model = Persona
		fields = (
			'run',
			'nombre',
			'apellido',
			'fechaNacimiento',
			'correo',
			'telefono',
			'region',
			'ciudad',
			'tipoVivienda',
			'username',
			'password',
			'password1'
			)

		labels = {
			'run' : 'Run',
			'nombre' : 'Nombre',
			'apellido' : 'Apellido',
			'fechaNacimiento' : 'Fecha de Nacimiento',
			'correo' : 'Correo',
			'telefono' : 'Telefono',
			}

	


class LoginForm(AuthenticationForm):

	password = forms.CharField(widget=forms.PasswordInput, label='Contraseña')
	

	class Meta:
		model = Persona
		fields = ('run', 'password')

		labels = {
			'run' : 'run',
			'password' : 'Contraseña'
			}

class AgregarForm(forms.ModelForm):
	

	class Meta:
		model = Rescatado
		fields = (
			
			'nombre',
			'razaPredominante',	
			'fotografia',
			'descripcion',
			'estado'
			)

		labels = {
			'fotografia' : '',	
			'nombre' : 'Nombre',
			'razaPredominante' : 'Raza Predominante',
			'descripcion' : 'Descripcion',
			'estado' : 'Estado'
			
			}

	

		
