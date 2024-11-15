from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from personajes.Forms import Formvaquero, formArma, formcaballo
from personajes.models import vaquero, arma,caballo 

# Base views
def index(request):
    return render(request, 'index.html')
def prueba(request):
    return render(request, 'prueba.html')

# Vaquero  views
def lista_vaquero(request):
    vaqueros = vaquero.objects.all()
    return render(request, 'lista.html', {'vaqueros': vaqueros})

def agregar_vaquero(request):
    if request.method == 'POST':
        form = Formvaquero(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/lista')
    else:
        form = Formvaquero()
    return render(request, 'agregar.html', {'form': form})

def eliminar_vaquero(request, id):
    vaqueroe = get_object_or_404(vaquero, id=id)
    vaqueroe.delete()
    return redirect('/lista')

def actualizar_vaquero(request, id):
    # Obtener el vaquero a actualizar
    vaqueroe = get_object_or_404(vaquero, id=id)
    
    # Obtener las armas y caballos asociados a este vaquero usando el campo vaquero_id
    armas = arma.objects.filter(vaquero_id=vaqueroe.id)
    caballos = caballo.objects.filter(vaquero_id=vaqueroe.id)
    
    # Procesar el formulario de actualización de vaquero
    if request.method == 'POST':
        form = Formvaquero(request.POST, instance=vaqueroe)
        if form.is_valid():
            form.save()  # Guardar los cambios en el vaquero
            return redirect('/lista')  # Redirigir a la lista de vaqueros
    else:
        form = Formvaquero(instance=vaqueroe)  # Crear el formulario con los datos del vaquero
    
    # Renderizar la plantilla con el formulario, armas y caballos asociados
    return render(request, 'modificar.html', {
        'form': form,
        'vaqueroe': vaqueroe,
        'armas': armas,
        'caballos': caballos,
        'id': id, 
    })

# Arma  views
def lista_armas(request):
    armas = arma.objects.all()
    return render(request, 'arma/armas.html', {'armas': armas})

def agregar_arma(request):
    form = formArma()  
    if request.method == 'POST':
        form = formArma(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/arma')
    return render(request, 'arma/agregar_arma.html', {'form': form})


def eliminar_arma(request, id):
    armae = get_object_or_404(arma, id=id)
    armae.delete()
    return redirect('/arma')

def actualizar_arma(request, id):
    arma2 = get_object_or_404(arma, id=id)
    if request.method == 'POST':
        form = formArma(request.POST, instance=arma2)
        if form.is_valid():
            form.save()
            return redirect('/arma')
    else:
        form = formArma(instance=arma2)
    return render(request, 'arma/actualizararma.html', {'form': form})



# Caballo views
def lista_caballos(request):
    caballos = caballo.objects.all()
    return render(request, 'caballo/caballos.html', {'caballos': caballos})

def agregar_caballo(request):
    if request.method == 'POST':
        form = formcaballo(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/caballosos')
    else:
        form = formcaballo()
    return render(request, 'caballo/agregarcaballo.html', {'form': form})

def eliminar_caballo(request, id):
    caballoe = get_object_or_404(caballo, id=id)
    caballoe.delete()
    return redirect('/caballosos')

def actualizar_caballo(request, id):
    caballoe = get_object_or_404(caballo, id=id)
    if request.method == 'POST':
        form = formcaballo(request.POST, instance=caballoe)
        if form.is_valid():
            form.save()
            return redirect('/caballosos')
    else:
        form = formcaballo(instance=caballoe)
    return render(request, 'caballo/modificarcaballo.html', {'form': form})


def desligar_Caballo(request, id):
    print(id)
    caballo_obj = get_object_or_404(caballo, id=id) 
    caballo_obj.vaquero_id = None
    caballo_obj.save()  
    return redirect(request.META.get('HTTP_REFERER', '/'))  

def desligar_Arma(request, id):
    print(id)
    arma_obj = get_object_or_404(arma, id=id)  
    arma_obj.vaquero_id = None  
    arma_obj.save() 
    return redirect(request.META.get('HTTP_REFERER', '/'))  


def agregar_caballo_vaquero(request, id,id_vaquero):
    print(id)
    caballo_obj = get_object_or_404(caballo, id=id) 
    caballo_obj.vaquero_id = id_vaquero
    caballo_obj.save()  
    return redirect(request.META.get('HTTP_REFERER', '/'))  

def agregar_arma_vaquero(request, id,id_vaquero):
    print(id)
    arma_obj = get_object_or_404(arma, id=id)  
    arma_obj.vaquero_id = id_vaquero  
    arma_obj.save() 
    return redirect(request.META.get('HTTP_REFERER', '/'))  