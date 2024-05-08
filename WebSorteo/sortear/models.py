from django.db import models

# Create your models here.

class ImagenPremio(models.Model):
      
    imagen = models.ImageField(upload_to="sorteo")
    def __str__(self):
        return f'Imagen {self.id}'

class PremioSorteo(models.Model):
    nombre = models.CharField(max_length=50,blank=False,default="premio")
    descripcion= models.TextField(max_length=200, default="descripcion")   
    imagenes = models.ForeignKey(ImagenPremio, blank=True, null=True, on_delete=models.SET_NULL)


class CategoriaPremio(models.Model):
    nombre = models.CharField(max_length=25)   
    premios = models.ForeignKey(PremioSorteo,null=True, on_delete=models.SET_NULL)   
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True)

    class Meta():
        verbose_name = "categoriaPremio"
        verbose_name_plural = "categoriasPremios"

    def __str__(self) :
        return self.nombre

class Sorteo(models.Model):
    nombre = models.CharField(max_length=25)
    descripcion=models.TextField(max_length=500)
    precio = models.FloatField()
    premios = models.ForeignKey(PremioSorteo, null=True, on_delete=models.SET_NULL)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=True) 

    class Meta():
        verbose_name = "sorteo"
        verbose_name_plural = "sorteos"

    def __str__(self) :
        return self.nombre
        



    

    


# https://coffeebytes.dev/es/como-subir-multiples-imagenes-en-django/ == enlace para poder subir varias fotos en el formulario
# http://blog.enriqueoriol.com/2014/07/upload-de-imagenes-con-django.html == otro tutorial