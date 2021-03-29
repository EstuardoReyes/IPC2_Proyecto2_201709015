class NodoMatriz():

    def __init__(self,dato,fila,columna):
        self.dato = dato
        self.fila = fila
        self.columna = columna
        self.siguiente = None
        self.atras = None
        self.arriba = None
        self.abajo = None

    def getDato(self):
        return self.dato
    
    

    