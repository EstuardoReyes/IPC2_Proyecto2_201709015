from NodoEncabezado import NodoEncabezado

class ListaDoble():
    

    def __init__(self):
        self.primero = None
        self.ultimo = None
        
    def Vacia(self):
        return self.primero == None
    
    def Agregar(self,dato):
        if self.Vacia():
            self.primero = self.ultimo = dato
        else: 
            aux = self.ultimo
            aux1 = self.ultimo
            self.ultimo = aux.siguiente = dato
            self.ultimo.atras = aux1

    def Buscar(self,identificador):
        aux = self.primero
        if self.primero == self.ultimo:
            if identificador == aux.identificador:
                return aux
        else:
            while aux != self.ultimo:
                if identificador == aux.identificador:
                    return aux
                aux = aux.siguiente
    
               
    def ExisteNodo(self,identificador):
        aux = self.primero
        if aux == None :
            return False
        else:  
            if self.primero == self.ultimo:
                print(identificador)
                print(aux.identificador)
                if identificador == aux.identificador:
                    return True
            else:
                while aux != self.ultimo:
                    if identificador == aux.identificador:
                        return True
                    aux = aux.siguiente
            return False






    def get_Primero(self):
        return self.primero

   

    
    