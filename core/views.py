from django.shortcuts import render
from django.http import HttpRequest
from .forms import JogadorForm

# Create your views here.

def index(request):
    return render(request, 'user/index.html')

def criar(request):
    if request.method == 'GET':
        form = JogadorForm()
        context = {
            'form': form
        }        
    return render(request, 'user/criar.html', context=context)