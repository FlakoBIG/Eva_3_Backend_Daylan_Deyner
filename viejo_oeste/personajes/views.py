from django.shortcuts import render , redirect
from personajes.Forms import Formvaquero , formArma,formcaballo
from personajes.models import vaquero , arma,caballo

#Vaquero

def index(request):
    return render(request,'index.html')

def lista(request):
    vaqueros = vaquero.objects.all()
    data = {'vaqueros':vaqueros}
    return render(request,'lista.html',data)

def agregar(request):
    form = Formvaquero()
    if request.method == 'POST':
        form = Formvaquero(request.POST)
        if form.is_valid():
            form.save()
            return lista(request)
    data = {'form':form}
    return render(request,'agregar.html',data)

def eliminar(request,id):
    P = vaquero.objects.get(id=id)
    P.delete()
    return lista(request)

def actualizar(request,id):
    P = vaquero.objects.get(id=id)
    form = Formvaquero(instance=P)
    if request.method=='POST':
        form = Formvaquero(request.POST,instance=P)
        if form.is_valid():
            form.save()
            return lista(request)
    data={'form':form}
    return render(request,'modificar.html',data)

def prueba(request):
    return render(request,'prueba.html')

#Arma

def index(request):
    return render(request,'index.html')

def arms(request):
    armas=arma.objects.all()
    data={'armas':armas}
    return render(request,'armas.html',data)

def agregararma(request):
    form = formArma(request.POST or None)  
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/arma')
    data = {'form': form}
    return render(request, 'agregar.html', data)

def eliminar(request,id):
    form=arma.objects.get(id=id)
    form.delete()
    return arms(request)

def actualizar(request,id):
    caball=arma.objects.get(id=id)
    form=formArma(instance=caball)
    if request.method=='POST':
        form=formArma(request.POST or None,instance=caball)
        if form.is_valid():
            form.save()
            return redirect('/arma')
    data={'form':form}
    return render (request,'agregar.html',data)

#Caballo

def index(request):
    return render(request,'index.html')

def caballos(request):
    form=caballo.objects.all()
    data={'caballos':form}
    return render(request,'caballos.html',data)

def agregarcaballos(request):
    form = formcaballo(request.POST or None)  
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('/caballosos')

    data = {'form': form}
    return render(request, 'agregarcaballo.html', data)
    
def eliminar(request,id):
    form=caballo.objects.get(id=id)
    form.delete()
    return caballos(request)

def actualizar(request,id):
    caball=caballo.objects.get(id=id)
    form=formcaballo(instance=caball)
    if request.method=='POST':
        form=formcaballo(request.POST or None,instance=caball)
        if form.is_valid():
            form.save()
            return redirect('/caballosos')
    data={'form':form}
    return render (request,'agregarcaballo.html',data)