from django.db import models
from django import forms
from django.contrib.auth.models import User
from django.conf import settings
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
	nombre = models.CharField(max_length=40)
	descripcion = models.TextField()

	def __str__(self):
		return self.nombre


#Tabla Rescatado
class Rescatado(models.Model):
	
	nombre = models.CharField(max_length=30, blank=False)
	razaPredominante = models.CharField(max_length=30)
	fotografia = models.FileField(blank=True)
	descripcion = models.TextField()
	estado = models.ForeignKey(Estado, on_delete = models.CASCADE)

	def __str__(self):
		return self.nombre


#Tabla Ciudad
class Ciudad(models.Model):
	nombre = models.CharField(max_length=20)
	region = models.ForeignKey(Region, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre


#Tabla Usuario
class Persona(models.Model):
	user = models.OneToOneField(User, on_delete= models.CASCADE)
	run = models.IntegerField(unique=True)
	nombre = models.CharField(max_length=30)
	apellido = models.CharField(max_length=40)
	fechaNacimiento = models.DateField()
	telefono = models.IntegerField()
	correo = models.EmailField()
	region = models.ForeignKey(Region, on_delete=models.CASCADE)
	ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
	tipoVivienda = models.ForeignKey(TipoVivienda, on_delete=models.CASCADE)
	

	def __str__(self):
		return (self.nombre + " " + self. apellido)

#Tabla RegistroAdopcion

class RegistroAdopcion(models.Model):
	run = models.ForeignKey(Persona, on_delete=models.CASCADE)
	rescatado = models.ForeignKey(Rescatado, on_delete=models.CASCADE)

	def __str__(self):
		return (self.run + " " +self.rescatado)()