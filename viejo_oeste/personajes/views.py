from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from personajes.Forms import Formvaquero, formArma, formcaballo
from personajes.models import vaquero, arma,caballo 

# Base views
def index(request):
    return render(request, 'index.html')
def prueba(request):
    return render(request, 'prueba.html')

# Vaquero (Cowboy) views
def lista_vaquero(request):
    vaqueros = vaquero.objects.all()
    return render(request, 'lista.html', {'vaqueros': vaqueros})

def agregar_vaquero(request):
    if request.method == 'POST':
        form = Formvaquero(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vaquero agregado exitosamente.')
            return redirect('/lista')
        messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = Formvaquero()
    return render(request, 'agregar.html', {'form': form})

def eliminar_vaquero(request, id):
    vaqueroe = get_object_or_404(vaquero, id=id)
    try: 
        vaqueroe.delete()
        messages.success(request, 'Vaquero eliminado exitosamente.')
    except Exception as e:
        messages.error(request, f'Error al eliminar el vaquero: {str(e)}')
    return redirect('/lista')

def actualizar_vaquero(request, id):
    vaqueroe = get_object_or_404(vaquero, id=id)
    if request.method == 'POST':
        form = Formvaquero(request.POST, instance=vaqueroe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Vaquero actualizado exitosamente.')
            return redirect('/lista')
        messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = Formvaquero(instance=vaqueroe)
    return render(request, 'modificar.html', {'form': form})

# Arma (Weapon) views
def lista_armas(request):
    armas = arma.objects.all()
    return render(request, 'arma/armas.html', {'armas': armas})

def agregar_arma(request):
    if request.method == 'POST':
        form = formArma(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Arma agregada exitosamente.')
            return redirect('/arma')
        messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = formArma()
    return render(request, 'arma/agregar_arma.html', {'form': form})

def eliminar_arma(request, id):
    armae = get_object_or_404(arma, id=id)
    try:
        armae.delete()
        messages.success(request, 'Arma eliminada exitosamente.')
    except Exception as e:
        messages.error(request, f'Error al eliminar el arma: {str(e)}')
    return redirect('lista_armas')

def actualizar_arma(request, id):
    arma2 = get_object_or_404(arma, id=id)
    if request.method == 'POST':
        form = formArma(request.POST, instance=arma2)
        if form.is_valid():
            form.save()
            messages.success(request, 'Arma actualizada exitosamente.')
            return redirect('lista_armas')
        messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = formArma(instance=arma2)
    return render(request, 'arma/agregar_arma.html', {'form': form})



# Caballo (Horse) views
def lista_caballos(request):
    caballos = caballo.objects.all()
    return render(request, 'caballo/caballos.html', {'caballos': caballos})

def agregar_caballo(request):
    if request.method == 'POST':
        form = formcaballo(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Caballo agregado exitosamente.')
            return redirect('/caballosos')
        messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = formcaballo()
    return render(request, 'caballo/agregarcaballo.html', {'form': form})

def eliminar_caballo(request, id):
    caballoe = get_object_or_404(caballo, id=id)
    try:
        caballoe.delete()
        messages.success(request, 'Caballo eliminado exitosamente.')
    except Exception as e:
        messages.error(request, f'Error al eliminar el caballo: {str(e)}')
    return redirect('/caballosos')

def actualizar_caballo(request, id):
    caballoe = get_object_or_404(caballo, id=id)
    if request.method == 'POST':
        form = formcaballo(request.POST, instance=caballoe)
        if form.is_valid():
            form.save()
            messages.success(request, 'Caballo actualizado exitosamente.')
            return redirect('/caballosos')
        messages.error(request, 'Por favor corrija los errores en el formulario.')
    else:
        form = formcaballo(instance=caballoe)
    return render(request, 'caballo/agregarcaballo.html', {'form': form})