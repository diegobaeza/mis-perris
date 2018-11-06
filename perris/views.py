from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *
from django.contrib.auth import authenticate, login as auth_login
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.views.generic import CreateView, ListView, UpdateView, DeleteView
from django.urls import reverse_lazy



# Create your views here.
def index(request):
    return render(request, 'perris/index.html', {})

def principal(request):
	return render(request, 'perris/Principal.html')

def registro(request):
	if request.method == 'POST':
		form = RegistroForm(request.POST)
		

		if form.is_valid():
			
			user = User.objects.create_user(first_name=form.cleaned_data['nombre'],last_name=form.cleaned_data['apellido'],username=form.cleaned_data['username'],password=form.cleaned_data['password'], email=form.cleaned_data['correo'])
				
			user.is_staff = False
			user.save()
				
			persona = Persona(user = user,
						run = form.cleaned_data['run'],
						nombre = form.cleaned_data['nombre'],
						apellido = form.cleaned_data['apellido'],
						fechaNacimiento = form.cleaned_data['fechaNacimiento'],
						telefono = form.cleaned_data['telefono'],
						correo = form.cleaned_data['correo'],
						region = form.cleaned_data['region'],
						ciudad = form.cleaned_data['ciudad'],
						tipoVivienda = form.cleaned_data['tipoVivienda']
						)

			persona.save()
			return redirect(principal)

	else:

		form = RegistroForm()
	return render(request, 'perris/Registro.html', {'form' : form})

def login(request):

	if request.method == 'POST':
		forml = AuthenticationForm(request.POST)

		
		username = request.POST['username']
		password = request.POST['password']

		access = authenticate(username=username, password=password)
	
		if access is not None:
			if access.is_active:
				auth_login(request, access)
				
				if access.is_staff:

					return HttpResponseRedirect('/administracion/')

				return HttpResponse('Logeado')
			else:
				
				return HttpResponse('Cuenta Inactiva')
		else:
			return HttpResponse('Usuario o contraseña incorrectos')
			

	else:
		
		forml = AuthenticationForm()

	return render(request, 'perris/login.html', {'forml': forml})


def administracion(request):
	if request.method == 'POST':
		form = AgregarForm(request.POST)
		
		if form.is_valid():
			
			return redirect(principal)

	else:

		form = AgregarForm()


	return render(request, 'perris/Administracion.html', {'form' : form})



def agregarMascota(request):
	if request.method == 'POST':
		form = AgregarForm(request.POST)
		
		if form.is_valid():

			rescatado = Rescatado(fotografia = form.cleaned_data['fotografia'],
						nombre = form.cleaned_data['nombre'],
						razaPredominante = form.cleaned_data['razaPredominante'],
						descripcion = form.cleaned_data['descripcion'],
						estado = form.cleaned_data['estado']
						)

			rescatado.save()
			return redirect(principal)

	else:

		form = AgregarForm()


	return render(request, 'perris/agregar.html', {'form' : form})


class ListaRescatado(ListView):
	model = Rescatado
	template_name = 'perris/lista_rescatado.html'


class RescatadoUpdate(UpdateView):
	model = Rescatado
	form_class = AgregarForm
	template_name = 'perris/editar.html'
	success_url = reverse_lazy('listaRescatado')


class RescatadoDelete(DeleteView):
	model = Rescatado
	template_name = 'perris/eliminar.html'
	success_url = reverse_lazy('listaRescatado')

