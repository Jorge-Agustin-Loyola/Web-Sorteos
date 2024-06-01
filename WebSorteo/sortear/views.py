from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import Formulario_Sorte,Formulario_Premio
from .listapremios import Contador
from .models import Sorteo,PremioSorteo,CategoriaPremio,ImagenPremio
import uuid
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
                    
                    # guardamos imagenes en la base de datos relacionadas a los corespondientes premios
                    premio = PremioSorteo.objects.last()
                    for i in x[3]:
                        ImagenPremio.objects.create(imagen=i , premio=premio)


                n="guardado_con_exito"
                url = reverse('sortear') + '?n={}'.format(n)
                return redirect(url)

    # REQUEST.METHOD == GET        
    else:
        # el parametro n puede ser asignado desde la funcion agregar_premio o quitar_premio
        
        n = request.GET.get('n')
        
        
        if n=="valido":

            formulario_sorteo = Formulario_Sorte(initial=valores_borrador)
            
        elif n=="guardado_con_exito":
           
           return render(request,"sortear/sortear.html", {'guardado':True})
            
        else:

            formulario_sorteo = Formulario_Sorte()

    lista_premios = listaDePremios.obtenerLista()
   
    return render(request,"sortear/sortear.html", {'f_sorteo': formulario_sorteo,'lista_premios': lista_premios, 'guardado':False})
    
    #https://www.pudn.com/Download/item/id/1694413197137756.html para subir muchas imagens


# carga el fomulario para agregar los premios del sorteo

def agregar_premio(request):
    formulario_premio = Formulario_Premio()

    # Con post recupero los datos el formulario agregar premio y los agrego a la lista de premios 

    if request.method == 'POST':
        formulario_premio = Formulario_Premio(request.POST, request.FILES)
        print(request.FILES)
        if formulario_premio.is_valid():
            nombre = request.POST.get('nombre_premio')
            categoria = request.POST.get("categorias_premio")
            descripcion = request.POST.get('descripcion_premio')
            images=request.FILES.getlist('imagen_premio')
            imagenes = []
            for image in images:
                    # Obtener el nombre original del archivo
                original_filename = image.name
                # Generar un nuevo nombre de archivo con un UUID aleatorio
                unique_filename = str(uuid.uuid4()) + "_" + original_filename
                # Asignar el nuevo nombre al archivo
                image.name = unique_filename
                imagenes.append(image.name)

            premio = {
                "nombre": nombre,
                "categoria": categoria,
                "descripcion": descripcion,
                "imagenes" : imagenes
            }

            listaDePremios.aumentar(premio)
            print("AUMENTO PREMIO")
            print(imagenes)
            # redirijo una a sortear con un parametro n = valido para trabajar con condicionales en la vista sortear
            n="valido"
            url = reverse('sortear') + '?n={}'.format(n)
            return redirect(url)
    
    return render(request, "sortear/premio.html", {"f_premio":formulario_premio})


#Esta funcion quita el premio de la lista de premios 
def quitar_premio(request,id):

    # elmino un premio de la lista recibendo como parametro el id correspondiente    
    listaDePremios.disminuir(id)
    
    # redirijo una a sortear con un parametro n = valido para trabajar con condicionales en la vista sortear
    n="valido"
    url = reverse('sortear') + '?n={}'.format(n)
    return redirect(url)



