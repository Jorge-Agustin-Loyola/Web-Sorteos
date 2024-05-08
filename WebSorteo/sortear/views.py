from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import Formulario_Sorte,Formulario_Premio
from .premio import Contador
# Create your views here.

# Inicializamos algunas variables
listaDePremios = Contador()
valores_borrador = None



def sortear(request):

    global valores_borrador

    if request.method == "POST":

        if "btn_agregarPremio" in request.POST:

            valores_borrador = {
                "nombre_sorteo":request.POST.get("nombre_sorteo"),
                "descripcion_sorteo":request.POST.get("descripcion_sorteo"),
                "precio_sorteo": request.POST.get("precio_sorteo"),
            }

            return redirect("agregarPremio")
        
        elif "btn_enviar" in request.POST:
            
            formulario = Formulario_Premio(request.POST)
            
            if formulario.is_valid():
                pass


        
        
            
    # REQUEST.METHOD == GET        
    else:

        n = request.GET.get('n')

        if n=="valido":

            formulario_sorteo = Formulario_Sorte(initial=valores_borrador)

        else:

            formulario_sorteo = Formulario_Sorte()

    lista_premios = listaDePremios.obtenerLista()

    return render(request,"sortear/sortear.html", {'f_sorteo': formulario_sorteo,'lista_premios': lista_premios})
    
    #https://www.pudn.com/Download/item/id/1694413197137756.html para subir muchas imagens



def agregar_premio(request):
    formulario_premio = Formulario_Premio()

    if request.method == 'POST':
        formulario_premio = Formulario_Premio(data=request.POST)
        if formulario_premio.is_valid():
            nombre = request.POST.get('nombre_premio')
            categoria = request.POST.get("categorias_premio")
            descripcion = request.POST.get('descripcion_premio')

        premio = {
            "nombre": nombre,
            "categoria": categoria,
            "descripcion": descripcion,
        }

        listaDePremios.aumentar(premio)

        n="valido"
        url = reverse('sortear') + '?n={}'.format(n)
        return redirect(url)

    return render(request, "sortear/premio.html", {"f_premio":formulario_premio})

# def agregar_premio(request):
       
#     formulario.aumentar(Formulario_Premio())
#     n="valido"
#     url = reverse('sortear') + '?n={}'.format(n)
#     return redirect(url)

def quitar_premio(request,id):
        
    listaDePremios.disminuir(id)
    

    n="valido"
    url = reverse('sortear') + '?n={}'.format(n)
    return redirect(url)



