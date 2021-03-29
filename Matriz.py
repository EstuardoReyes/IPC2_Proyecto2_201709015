from Nodo import Nodo
from ListaDoble import ListaDoble
from NodoMatriz import NodoMatriz
from NodoEncabezado import NodoEncabezado


class Matriz():
    

    def __init__(self,nombre):
        listaDeListas = ListaDoble()
        listaDeColumna = ListaDoble()
        self.primero = Nodo(nombre,listaDeListas,listaDeColumna)


    def Search(self,fila,columna):
        print("buscar "+str(fila)+ "   "+str(columna))
        fil = self.primero.fila.Buscar(fila).Nodo
        col = self.primero.columna.Buscar(columna).Nodo
        encontrado = False
        while True:
            while True:
                if fil == col:
                    return fil
                    encontrado = True
                    break
                elif fil.siguiente == None:
                    break
                else:
                    fil = fil.siguiente
            if col.abajo == None:
                return False
                break
            col = col.abajo
            if encontrado:
                break
        
    def Agregar(self,fila,columna,valor):
        nodoMatriz = NodoMatriz(valor,fila,columna) 
        if self.primero.fila.ExisteNodo(fila) and self.primero.columna.ExisteNodo(columna): #si existe el nodo
            aux = self.primero.fila.Buscar(fila)
            aux1 = aux.Nodo
            aux2 = self.primero.columna.Buscar(columna)
            aux3 = aux2.Nodo
            while aux1.siguiente != None:
                aux1 = aux1.siguiente
            aux1.siguiente = nodoMatriz
            nodoMatriz.atras = aux1
            if fila > 1:
                nodoMatriz.arriba = self.Search(fila,columna)
                nodoMatriz.arriba.abajo = nodoMatriz
        elif self.primero.fila.ExisteNodo(fila)  and self.primero.columna.ExisteNodo(columna) == False: #si existe el nodo
            aux = self.primero.fila.Buscar(fila)
            aux1 = aux.Nodo
            nodoCabezacolumna = NodoEncabezado(columna)
            nodoCabezacolumna.Nodo = nodoMatriz
            self.primero.columna.Agregar(nodoCabezacolumna)
            while aux1.siguiente != None:
                aux1 = aux1.siguiente
            aux1.siguiente = nodoMatriz
            nodoMatriz.atras = aux1
        elif self.primero.fila.ExisteNodo(fila) == False and self.primero.columna.ExisteNodo(columna): #si existe el nodo
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
            nodoCabezafila = NodoEncabezado(fila)
            nodoCabezafila.Nodo = nodoMatriz
            self.primero.fila.Agregar(nodoCabezafila)
            nodoCabezacolumna = NodoEncabezado(columna)
            nodoCabezacolumna.Nodo = nodoMatriz
            self.primero.columna.Agregar(nodoCabezacolumna)

    def Print(self):
        print("Deberia imprimir aqui")

    def get_Primero(self):
        return self.primero