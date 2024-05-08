
# Esta clase lo que hace es crear y modifcar la lista de premios para visualizarlos en el formulario para crear un sorteo (sortear.html)
class Contador:
    def __init__(self, listaPremios={},contador=0):
        self.listaPremios = listaPremios
        self.contador = contador
       
    def aumentar(self, premio):
        self.contador+=1
        self.listaPremios[self.contador]= premio

       
        

    
    


    def disminuir(self,id):
        
        del self.listaPremios[id]

        # Una vez eliminado un premio de la lista esta se reordena

        i=1
        lista_id_nuevo = {}
        for valor in self.listaPremios.values():
            lista_id_nuevo[i]=valor
            i+=1
        
        self.listaPremios = lista_id_nuevo
        self.contador = i-1
    

    def obtenerLista(self):
        return self.listaPremios