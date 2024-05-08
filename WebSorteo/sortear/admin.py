from django.contrib import admin
from .models import Sorteo, CategoriaPremio,ImagenPremio, PremioSorteo
# Register your models here.

# class ImagenPremioInline(admin.TabularInline):
#     model = ImagenPremio
#     extra = 3
    

    

class CategoriaPremioAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")


class SorteoAdmin(admin.ModelAdmin):
    readonly_fields = ("created","updated")



    


    
    


admin.site.register(Sorteo,SorteoAdmin)
admin.site.register(CategoriaPremio,CategoriaPremioAdmin)
admin.site.register(PremioSorteo)
admin.site.register(ImagenPremio)
