from django.shortcuts import render, redirect
from .forms import CuadroForm, EsculturaForm, CeramicaForm

def crear_cuadro(request):
    if request.method == 'POST':
        form = CuadroForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_cuadros')
    else: 
        form = CuadroForm()
        return render(request, 'crear_cuadro.html', {'form': form})

def crear_escultura(request):
    if request.method == 'POST':
        form = EsculturaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_esculturas')
    else: 
        form = CuadroForm()
        return render(request, 'crear_escultura.html', {'form': form})
    
def crear_ceramica(request):
    if request.method == 'POST':
        form = CeramicaForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('lista_ceramicas')
    else: 
        form = CeramicaForm()
        return render(request, 'crear_ceramica.html', {'form': form})