from django.shortcuts import render, redirect, get_object_or_404
from .models import Usuario
from .forms import *

# Create your views here.
def index(request):
    return render(request, 'perris/index.html', {})

def principal(request):
	return render(request, 'perris/Principal.html')

def registro(request):
	if request.method == 'POST':
		form = RegistroForm(request.POST)

		if form.is_valid():
			post = form.save(commit=False)
			post.save()

			return redirect(principal)

	else:

		form = RegistroForm()
	return render(request, 'perris/Registro.html', {'form' : form})



