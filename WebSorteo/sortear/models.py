from django.db import models

# Create your models here.

class Sorteo(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion=models.TextField(max_length=500)
    precio = models.FloatField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True) 

    class Meta():
        verbose_name = "sorteo"
        verbose_name_plural = "sorteos"

    def __str__(self) :
        return self.nombre

        
class CategoriaPremio(models.Model):
    nombre = models.CharField(max_length=25)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = "categoriaPremio"
        verbose_name_plural = "categoriasPremios"

    def __str__(self) :
        return self.nombre

class PremioSorteo(models.Model):
    nombre = models.CharField(max_length=50,blank=False,default="premio")
    descripcion= models.TextField(max_length=200, default="descripcion")
    categoria = models.ForeignKey(CategoriaPremio,null=True, on_delete=models.SET_NULL)  
    sorteo = models.ForeignKey(Sorteo, null=True, on_delete=models.SET_NULL)


class ImagenPremio(models.Model):      
    imagen = models.ImageField(upload_to="sorteo")
    premio = models.ForeignKey(PremioSorteo, blank=True, null=True, on_delete=models.SET_NULL)
    def __str__(self):
        return f'Imagen {self.id}'


    

    


# https://coffeebytes.dev/es/como-subir-multiples-imagenes-en-django/ == enlace para poder subir varias fotos en el formulario
# http://blog.enriqueoriol.com/2014/07/upload-de-imagenes-con-django.html == otro tutorial