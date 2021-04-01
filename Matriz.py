from Nodo import Nodo
from ListaDoble import ListaDoble
from NodoMatriz import NodoMatriz
from NodoEncabezado import NodoEncabezado


class Matriz():
    

    def __init__(self,nombre,f,c):
        listaDeListas = ListaDoble()
        listaDeColumna = ListaDoble()
        self.primero = Nodo(nombre,listaDeListas,listaDeColumna,f,c)



    def Search(self,fila,columna):
        fil = self.primero.fila.Buscar(fila).Nodo
        col = self.primero.columna.Buscar(columna).Nodo
        while col != None:
            while fil != None:
                if fil == col:
                    return fil
                else:
                    fil = fil.siguiente
            fil = self.primero.fila.Buscar(fila).Nodo
            col = col.abajo
                
    def Agregar(self,fila,columna,valor):
        nodoMatriz = NodoMatriz(valor,fila,columna) 
        if self.primero.fila.ExisteNodo(fila,"fila") == False and self.primero.columna.ExisteNodo(columna,"Columna") == False: #si existe e
            nodoCabezacolumna = NodoEncabezado(columna)
            nodoCabezafila = NodoEncabezado(fila)
            nodoCabezacolumna.Nodo = nodoMatriz
            nodoCabezafila.Nodo = nodoMatriz
            self.primero.fila.Agregar(nodoCabezafila)
            self.primero.columna.Agregar(nodoCabezacolumna)
            
        elif self.primero.fila.ExisteNodo(fila,"fila")  and self.primero.columna.ExisteNodo(columna,"columna") == False: #si existe el no
            aux = self.primero.fila.Buscar(fila)
            aux1 = aux.Nodo
            nodoCabezacolumna = NodoEncabezado(columna)
            nodoCabezacolumna.Nodo = nodoMatriz
            self.primero.columna.Agregar(nodoCabezacolumna)
            while aux1.siguiente != None:
                aux1 = aux1.siguiente
            aux1.siguiente = nodoMatriz
            nodoMatriz.atras = aux1
            
        elif self.primero.fila.ExisteNodo(fila,"fila") == False and self.primero.columna.ExisteNodo(columna,"columna"): #si existe el nodo
            aux = self.primero.columna.Buscar(columna)
            aux1 = aux.Nodo
            nodoCabezaFila = NodoEncabezado(fila)
            nodoCabezaFila.Nodo = nodoMatriz
            self.primero.fila.Agregar(nodoCabezaFila)
            while aux1.abajo != None:
                aux1 = aux1.abajo
            aux1.abajo = nodoMatriz
            nodoMatriz.arriba = aux1
            

        else:
            auxiliar = self.primero.fila.Buscar(fila)
            aux1 = auxiliar.Nodo
            while aux1.siguiente != None:
                aux1 = aux1.siguiente
            aux1.siguiente = nodoMatriz
            nodoMatriz.atras = aux1
            aux = self.primero.columna.Buscar(columna)
            au = aux.Nodo
            while au.abajo != None:
                au = au.abajo
            au.abajo = nodoMatriz
            nodoMatriz.arriba = au

    def Pintando(self):
        au = self.primero.fila.primero   
        texto = ''   
        while(au != None):
            auxiliar = au.Nodo
            while(auxiliar != None):
                texto = texto + auxiliar.dato
                auxiliar = auxiliar.siguiente
            au = au.siguiente
            texto = texto + '\n'
        return texto

    def Print(self):
        print(self.primero.nombre)
        print(" c ",end="")
        aux = self.primero.columna.primero
        while (aux != None):
            print(str(aux.identificador)+"  ", end="")
            aux = aux.siguiente
        print("")
        au = self.primero.fila.primero      
        while(au != None):
            print(str(au.identificador)+"  ", end = "")
            auxiliar = au.Nodo
            while(auxiliar != None):
                print(auxiliar.dato+"  ", end = "")
                auxiliar = auxiliar.siguiente
            au = au.siguiente
            print("")

    def get_Primero(self):
        return self.primero
    
    def Imprimir(self,posicion,identificador):
        if posicion == 'fila':
            auxiliar = self.primero.fila.Buscar(identificador)
            aux = auxiliar.Nodo
            print("Fila "+str(identificador)+": ")
            while aux != None:
                print(aux.dato+" ", end = "") 
                aux = aux.siguiente
            
        elif posicion == 'columna':
            auxiliar = self.primero.columna.Buscar(identificador)
            aux = auxiliar.Nodo
            print("Columna "+str(identificador)+": ")
            while aux != None:
                print(aux.dato+" ", end = "") 
                aux = aux.abajo
        print("")
    
    