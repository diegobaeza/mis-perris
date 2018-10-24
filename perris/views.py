from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'perris/index.html', {})

def principal(request):
	return render(request, 'perris/Principal.html',{})

