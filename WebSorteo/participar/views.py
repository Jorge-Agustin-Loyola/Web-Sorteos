from django.shortcuts import render
from sortear.models import Sorteo, PremioSorteo
# Create your views here.
def participar(request):
    sorteo = Sorteo.objects.all()
    return render(request,"participar/participar.html", {'sorteos':sorteo})

def verDetalle(request,id):
    sorteo = Sorteo.objects.filter(id = id).values()
    premios = PremioSorteo.objects.filter(sorteo_id = id).values()
    return render(request,"participar/verSorteo.html",{'sorteo':sorteo, 'premios':premios})