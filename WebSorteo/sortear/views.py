from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import Formulario_Sorte,Formulario_Premio
from .premio import Contador
from .models import Sorteo,PremioSorteo,CategoriaPremio
# Create your views here.

# Inicializamos algunas variables
listaDePremios = Contador()
valores_borrador = None



def sortear(request):

    global valores_borrador

    if request.method == "POST":

        if "btn_agregarPremio" in request.POST:

            # Estos valores se guardan para que se conserven en el formulario de sorteo cuando se recarge la pagina al agregar o quitar un premio
            valores_borrador = {
                "nombre_sorteo":request.POST.get("nombre_sorteo"),
                "descripcion_sorteo":request.POST.get("descripcion_sorteo"),
                "precio_sorteo": request.POST.get("precio_sorteo"),
            }

            return redirect("agregarPremio")
        
        elif "btn_enviar" in request.POST:
            
            formulario = Formulario_Sorte(request.POST)
            
            if formulario.is_valid():
                # Accediendo a los datos limpios y validos
                nombre = formulario.cleaned_data.get("nombre_sorteo")
                descripcion = formulario.cleaned_data.get("descripcion_sorteo")
                precio = formulario.cleaned_data.get("precio_sorteo")
                
                # Creando una instancia del modelo sorteo y premios y guardándola en la base de datos
                Sorteo.objects.create(nombre= nombre, descripcion=descripcion, precio=precio)
                
                
                # Este ciclo for anidado nos permite acceder a los premios guardados en la lista de premios para posteriormente guardarlos en la base de datos
                for id_premio, premio in listaDePremios.obtenerLista().items():
                    x = []
                    for key, value in premio.items():
                        x.append(value)

                    # instanciamos el objeto de categoria que corresponde al id que se guardo en el formulario para poder hacer las relaciones necesarias al guardar un premio en la base de datos    
                    categoria = CategoriaPremio.objects.filter(id=x[1])[0]

                    # instanciamos el ultimo objeto de sorteo para poder hacer las relaciones correspondiente al guardar un premio en la base de datos    
                    sorteo = Sorteo.objects.last()

                    # Guardamos el premio en la base de datos 
                    PremioSorteo.objects.create(nombre=x[0], categoria=categoria, descripcion=x[2], sorteo=sorteo)


                    n="valido"
                    url = reverse('sortear') + '?n={}'.format(n)
                    return redirect(url)

    # REQUEST.METHOD == GET        
    else:
        # el parametro n puede ser asignado desde la funcion agregar_premio o quitar_premio
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

    # Con post recupero los datos el formulario agregar premio y los agrego a la lista de premios 

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

        # redirijo una a sortear con un parametro n = valido para trabajar con condicionales en la vista sortear
        n="valido"
        url = reverse('sortear') + '?n={}'.format(n)
        return redirect(url)

    return render(request, "sortear/premio.html", {"f_premio":formulario_premio})



def quitar_premio(request,id):

    # elmino un premio de la lista recibendo como parametro el id correspondiente    
    listaDePremios.disminuir(id)
    
    # redirijo una a sortear con un parametro n = valido para trabajar con condicionales en la vista sortear
    n="valido"
    url = reverse('sortear') + '?n={}'.format(n)
    return redirect(url)



