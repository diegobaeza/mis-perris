from django.db import models
from django import forms
# Create your models here.

# Tabla Region
class Region(models.Model):
	nombre = models.CharField(max_length=40)


	def __str__(self):
		return self.nombre


#Tabla Estado

class Estado(models.Model):
	nombre = models.CharField(max_length=30)
	descripcion = models.TextField()

	def __str__(self):
		return self.nombre


#Tabla TipoUsuario
class TipoUsuario(models.Model):
	nombre = models.CharField(max_length=20)
	descripcion = models.TextField()

	def __str__(self):
		return self.nombre


#Tabla TipoVivienda
class TipoVivienda(models.Model):
	nombre = models.CharField(max_length=20)
	descripcion = models.TextField()

	def __str__(self):
		return self.nombre


#Tabla Rescatado
class Rescatado(models.Model):
	fotografia = models.FileField(blank=True)
	razaPredominante = models.CharField(max_length=30)
	descripcion = models.TextField()
	estado = models.ForeignKey(Estado, on_delete = models.CASCADE)

	def __str__(self):
		return self.fotografia


#Tabla Ciudad
class Ciudad(models.Model):
	nombre = models.CharField(max_length=20)
	region = models.ForeignKey(Region, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre


#Tabla Usuario
class Usuario(models.Model):
	run = models.IntegerField()
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=40)
	fechaNacimiento = models.DateField()
	telefono = models.IntegerField()
	correo = models.EmailField()
	region = models.ForeignKey(Region, on_delete=models.CASCADE)
	ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
	tipoVivienda = models.ForeignKey(TipoVivienda, on_delete=models.CASCADE)
	contrasena = forms.CharField(widget=forms.PasswordInput)
	tipoUsuario = models.ForeignKey(TipoUsuario, on_delete=models.CASCADE)

	def __str__(self):
		return (self.nombre + " " + self. apellidos)
#Tabla RegistroAdopcion

class RegistroAdopcion(models.Model):
	run = models.ForeignKey(Usuario, on_delete=models.CASCADE)
	rescatado = models.ForeignKey(Rescatado, on_delete=models.CASCADE)

	def __str__(self):
		return (self.run + " " +self.rescatado)