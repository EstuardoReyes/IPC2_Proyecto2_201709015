from tkinter import *
from tkinter import ttk
import copy
from tkinter.filedialog import askopenfilename
from tkinter.filedialog import askdirectory
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom
import xml.dom.minidom
from xml.etree import ElementTree
from graphviz import Digraph
import os
from ListaDoble import ListaDoble
from Matriz import Matriz
from tkinter import messagebox
from NodoLista import NodoLista

archivo_Seleccionado = False
salida = False
listaAlpha = []
listaImagenes = ListaDoble()
procesar = False
x1 = 0
y1 = 0
x2 = 0
y2 = 0
elementos = 0
filas = 0
columnas = 0



def prettify(elem):
    """Return a pretty-printed XML string for the Element.
    """
    rough_string = ElementTree.tostring(elem, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent="  ")

def cls():
    r=0
    while r<10:
        print("")
        r=r+1 

def carga():
    root = Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    #archivo = askopenfilename(filetypes =(("Archivo TXT", "*.txt"),("Todos Los Archivos","*.*")),title = "Busque su archivo.")
    root.update()
    root.destroy()
    xmldoc = xml.dom.minidom.parse("D:\Galeria\Escritorio\entrada1.txt")
    for n in xmldoc.getElementsByTagName("matriz"):
        for name in n.getElementsByTagName("nombre"):
            nombre = name.firstChild.data
            for fi in n.getElementsByTagName("filas"):
                fila = fi.firstChild.data
            for co in n.getElementsByTagName("columnas"):
                columna = co.firstChild.data
            for img in n.getElementsByTagName("imagen"):
                imagen = img.firstChild.data
            x = 0
            fi = 1
            state = 0
            colu = 1
            matriz = Matriz(nombre,fila,columna)
            error = False
            while x < len(imagen):
                actual = imagen[x]
                if state == 0:
                    if ord(actual) == 10 or ord(actual) == 9:
                        x = x + 1
                    elif ord(actual) == 45 or ord(actual) == 42:
                        state = 1
      #######################################################################################################
                elif state == 1:
                    if ord(actual) == 45: # guion
                        x = x + 1
                        if fi>int(fila) or colu>int(columna):
                            print("Error Matriz mayor que establecida")
                        else:
                            matriz.Agregar(fi,colu,'-')             
                    elif ord(actual) == 42: # asterisco
                        x = x + 1
                        if fi>int(fila) or colu>int(columna):
                            print("Error Matriz mayor que establecida")
                        else:
                            matriz.Agregar(fi,colu,'*')         
                    else:
                        fi = fi + 1
                        state = 0
                        colu = 0
                    colu = colu + 1
        Nodo = NodoLista(matriz,nombre,fila,columna)  
        listaImagenes.Agregar(Nodo)
        print("Se agrego Imagen: "+nombre)

def ventanaEmergente(texto): 
    messagebox.showinfo(message=texto, title="Avisos")

def close_window(objeto):
    objeto.destroy()

def operaciones():
    if listaImagenes.primero == None :
        ventanaEmergente("Porfavor Seleccione Carga Primero")
    else:
        windows = Tk()
        windows.title("Operaciones Validas")
        ancho_ventana = 700
        alto_ventana = 490
        x_ventana = raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = raiz.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        windows.geometry(posicion)
        Lb1 = ttk.Label(windows,text="Imagenes Existentes: ",font=("Lucida Console",15))
        Lb1.place(x=100,y=30)
        combo = ttk.Combobox(windows)
        combo.place(x=350,y=30)
        opciones = ['Seleccione Imagen']
        aux = listaImagenes.primero
        while aux != None:
            opciones.append(aux.nombre)
            aux = aux.siguiente
        combo['values']=opciones
        combo.current(0)
        windows.iconbitmap("codificacion.ico")
        button = ttk.Button(windows, text="ver",command = lambda: verImagen(combo))
        button.place(x=500,y=29)
        combo1 = ttk.Combobox(windows)
        combo1.place(x=90,y=170)
        opc = ['Seleccione Opcion','1. Rotacion Horizontal','2. Rotacion Vertical','3. Transpuesta','4. Limpiar Zona','5. Agregar Linea Horizontal','6. Agregar Linea Vertical','7. Agregar Rectangulo','8. Agregar Triangulo Rectangular']
        combo1['values']=opc
        combo1.current(0)
        i = ttk.Label(windows,text="Operaciones con 1 Imagen",font=("Lucida Console",15))
        i.place(x=20,y=100)
        combo2 = ttk.Combobox(windows)
        combo2.place(x=90,y=230)
        opcione = ['Seleccione Imagen']
        aux = listaImagenes.primero
        while aux != None:
            opcione.append(aux.nombre)
            aux = aux.siguiente
        combo2['values']=opcione
        combo2.current(0)
        ii = ttk.Label(windows,text="Operaciones con 2 Imagenes",font=("Lucida Console",15))
        ii.place(x=350,y=100)
        b1 = ttk.Button(windows,text="Calcular",command = lambda: operacion1(combo1,combo2,windows))
        b1.place(x=120,y=300)
        windows.mainloop()
        
def operacion1(combo1,combo2,ventana):

    global x1,x2,y1,y2,filas,columnas,elementos
    cb = combo1.get()
    cb2 = combo2.get()
    if cb == 'Seleccione Opcion':
        ventanaEmergente("Porfavor Seleccione una Opcion Valida")
    elif cb2 == 'Seleccione Imagen':
        ventanaEmergente("Porfavor Seleccione una Imagen Valida")
    else:
        tamaño = 25
        aux = listaImagenes.BuscarMatriz(cb2) # Nodo que cuenta con la matriz de aqui tengo que remplazar
        copy = aux.matriz
        matriz = aux.matriz
        if cb == '1. Rotacion Horizontal':
            newMatriz = Matriz(matriz.primero.nombre,matriz.primero.f,matriz.primero.c)
            fila = matriz.primero.f
            auxiliar = matriz.primero.fila.Buscar(int(fila))
            aux1 = auxiliar.Nodo
            fi = 1
            while aux1 != None:
                aux2 = aux1
                co = 1
                while aux2 != None:
                    newMatriz.Agregar(fi,co,aux2.dato)
                    aux2 = aux2.siguiente
                    co = co + 1
                aux1 = aux1.arriba
                fi = fi + 1
            aux.matriz = newMatriz
            t1 = matriz.Pintando()
            t2 = newMatriz.Pintando()
            ancho = 0.83*float(tamaño)*float(matriz.primero.c)
            alto = 1.36*float(tamaño)*float(matriz.primero.f)
            if alto >= 400 or ancho >= 300:
                while alto>= 380 or ancho >= 300 :
                    tamaño = tamaño-0.3
                    alto = 1.36*float(tamaño)*float(matriz.primero.f)
                    ancho = 0.83*float(tamaño)*float(matriz.primero.c)      
            px = (300-ancho)/2
            im1 = Label(raiz,text=t1,font=("Lucida Console",int(tamaño)))
            im1.place(x=px,y=90)
            im3 = Label(raiz,text="Imagen Original",font=("Lucida Console",10))
            im3.place(x=px+30,y=90+alto)
            px1 = ((300-ancho)/2)+340
            im2 = Label(raiz,text=t2,font=("Lucida Console",int(tamaño)))
            im2.place(x=px1,y=90)
            im4 = Label(raiz,text="Rotacion Horizontal",font=("Lucida Console",10))
            im4.place(x=px+370,y=90+alto)
            ventana.destroy()
        elif cb == '2. Rotacion Vertical':
            newMatriz = Matriz(matriz.primero.nombre,matriz.primero.f,matriz.primero.c)
            auxiliar = matriz.primero.fila.Buscar(1)
            aux1 = auxiliar.Nodo
            fi = 1
            while aux1 != None:
                auxili = aux1
                aux1 = aux1.siguiente
            while auxili != None:
                aux2 = auxili
                co = 1
                while aux2 != None:
                    newMatriz.Agregar(fi,co,aux2.dato)
                    aux2 = aux2.atras
                    co = co + 1
                auxili = auxili.abajo
                fi = fi + 1
            aux.matriz = newMatriz
            t1 = matriz.Pintando()
            t2 = newMatriz.Pintando()
            ancho = 0.83*float(tamaño)*float(matriz.primero.c)
            alto = 1.36*float(tamaño)*float(matriz.primero.f)
            if alto >= 400 or ancho >= 300:
                while alto>= 380 or ancho >= 300 :
                    tamaño = tamaño-0.3
                    alto = 1.36*float(tamaño)*float(matriz.primero.f)
                    ancho = 0.83*float(tamaño)*float(matriz.primero.c)      
            px = (300-ancho)/2
            im1 = Label(raiz,text=t1,font=("Lucida Console",int(tamaño)))
            im1.place(x=px,y=90)
            im3 = Label(raiz,text="Imagen Original",font=("Lucida Console",10))
            im3.place(x=px+30,y=90+alto)
            px1 = ((300-ancho)/2)+340
            im2 = Label(raiz,text=t2,font=("Lucida Console",int(tamaño)))
            im2.place(x=px1,y=90)
            im4 = Label(raiz,text="Rotacion Verticalmente",font=("Lucida Console",10))
            im4.place(x=px+350,y=90+alto)
            ventana.destroy()
        elif cb == '3. Transpuesta':
            newMatriz = Matriz(matriz.primero.nombre,matriz.primero.f,matriz.primero.c)
            fila = matriz.primero.f
            auxiliar = matriz.primero.fila.Buscar(1)
            aux1 = auxiliar.Nodo
            fi = 1
            while aux1 != None:
                aux2 = aux1
                co = 1
                while aux2 != None:
                    newMatriz.Agregar(fi,co,aux2.dato)
                    aux2 = aux2.abajo
                    co = co + 1
                aux1 = aux1.siguiente
                fi = fi + 1
            aux.matriz = newMatriz
            t1 = matriz.Pintando()
            t2 = newMatriz.Pintando()
            ancho = 0.83*float(tamaño)*float(matriz.primero.c)
            alto = 1.36*float(tamaño)*float(matriz.primero.f)
            if alto >= 400 or ancho >= 300:
                while alto>= 380 or ancho >= 300 :
                    tamaño = tamaño-0.3
                    alto = 1.36*float(tamaño)*float(matriz.primero.f)
                    ancho = 0.83*float(tamaño)*float(matriz.primero.c)      
            px = (300-ancho)/2
            im1 = Label(raiz,text=t1,font=("Lucida Console",int(tamaño)))
            im1.place(x=px,y=90)
            im3 = Label(raiz,text="Imagen Original",font=("Lucida Console",10))
            im3.place(x=px+30,y=90+alto)
            px1 = ((300-ancho)/2)+340
            im2 = Label(raiz,text=t2,font=("Lucida Console",int(tamaño)))
            im2.place(x=px1,y=90)
            im4 = Label(raiz,text="Transpuesta",font=("Lucida Console",10))
            im4.place(x=px+390,y=90+alto)
            ventana.destroy()
        elif cb == '4. Limpiar Zona':
            vent = Tk()
            vent.title("Ingreso de Datos")
            ancho = 360
            alto = 260     
            x_ventana = raiz.winfo_screenwidth() // 2 - int(ancho) // 2
            y_ventana = raiz.winfo_screenheight() // 2 - int(alto) // 2
            posicion = str(int(ancho)) + "x" + str(int(alto)) + "+" + str(x_ventana) + "+" + str(y_ventana)
            vent.geometry(posicion)
            lb = ttk.Label(vent,text="Ingrese los siguientes datos",font=("Lucida Console",14))
            lb.place(x=23,y=10)
            lb1 = ttk.Label(vent,text="Ingrese F:1 =",font=("Lucida Console",11))
            lb1.place(x=90,y=60)
            entry1 = ttk.Entry(vent,width=5)
            entry1.place(x=220,y=60)
            lb1 = ttk.Label(vent,text="Ingrese C:1 =",font=("Lucida Console",11))
            lb1.place(x=90,y=90)
            entry2 = ttk.Entry(vent,width=5)
            entry2.place(x=220,y=90)
            lb1 = ttk.Label(vent,text="Ingrese F:2 =",font=("Lucida Console",11))
            lb1.place(x=90,y=120)
            entry3 = ttk.Entry(vent,width=5)
            entry3.place(x=220,y=120)
            lb1 = ttk.Label(vent,text="Ingrese C:2 =",font=("Lucida Console",11))
            lb1.place(x=90,y=150)
            entry4 = ttk.Entry(vent,width=5)
            entry4.place(x=220,y=150)
            bo = ttk.Button(vent,text="Aceptar",command = lambda: guardar(ventana,vent,entry1.get(),entry2.get(),entry3.get(),entry4.get(),matriz.primero.f,matriz.primero.c,matriz))
            bo.place(x=140,y=200)
        elif cb == '5. Agregar Linea Horizontal':
            vent = Tk()
            vent.title("Ingreso de Datos")
            ancho = 360
            alto = 260     
            x_ventana = raiz.winfo_screenwidth() // 2 - int(ancho) // 2
            y_ventana = raiz.winfo_screenheight() // 2 - int(alto) // 2
            posicion = str(int(ancho)) + "x" + str(int(alto)) + "+" + str(x_ventana) + "+" + str(y_ventana)
            vent.geometry(posicion)
            lb = ttk.Label(vent,text="Ingrese los siguientes datos",font=("Lucida Console",14))
            lb.place(x=23,y=10)
            lb1 = ttk.Label(vent,text="Ingrese F =",font=("Lucida Console",11))
            lb1.place(x=90,y=60)
            entry1 = ttk.Entry(vent,width=5)
            entry1.place(x=220,y=60)
            lb1 = ttk.Label(vent,text="Ingrese C =",font=("Lucida Console",11))
            lb1.place(x=90,y=90)
            entry2 = ttk.Entry(vent,width=5)
            entry2.place(x=220,y=90)
            lb1 = ttk.Label(vent,text="Ingrese Cantidad de Elementos =",font=("Lucida Console",11))
            lb1.place(x=90,y=120)
            entry3 = ttk.Entry(vent,width=5)
            entry3.place(x=220,y=120)
            bo = ttk.Button(vent,text="Aceptar",command = lambda: agregarH(ventana,vent,entry1.get(),entry2.get(),entry3.get(),matriz.primero.f,matriz.primero.c,matriz))
            bo.place(x=140,y=200)
        #elif cb == '6. Agregar Linea Vertical':
        #elif cb == '7. Agregar Rectangulo':
        #elif cb == '8. Agregar Triangulo Rectangular':
def agregarH(ventana,windows,s1,s2,d1,f,c,matriz):
    auxiliar = copy.deepcopy(matriz)
    if s1.isdigit() and s2.isdigit() and d1.isdigit():
        if int(s1) <= int(c) and int(s1) >= 1 :
            if int(s2) <= int(f) and int(s2) >= 1 :
                if int(d1) <= int(c) and int(d1) >= 1 :
                    f1 = int(s1)
                    c1 = int(s2)
                    elementos = int(d1)
                    aux = matriz.Search(f1,c1)
                    i = 0
                    if int(c1)-int(elementos) >= 0:
                        while i <= elementos:
                            aux.dato = '*'
                            i = i + 1
                            aux = aux.atras
                     
                    elif int(c1)+int(elementos) <= int(c)+1:
                        while i <= elementos:
                            aux.dato = '*'
                            i = i + 1
                            aux = aux.siguiente
                    else:
                        ventanaEmergente("Elementos no cabe en matriz")
                    tamaño = 25
                    t1 = auxiliar.Pintando()
                    t2 = matriz.Pintando()
                    ancho = 0.83*float(tamaño)*float(matriz.primero.c)
                    alto = 1.36*float(tamaño)*float(matriz.primero.f)
                    if alto >= 400 or ancho >= 300:
                        while alto>= 380 or ancho >= 300 :
                            tamaño = tamaño-0.3
                            alto = 1.36*float(tamaño)*float(matriz.primero.f)
                            ancho = 0.83*float(tamaño)*float(matriz.primero.c)      
                    px = (300-ancho)/2
                    im1 = Label(raiz,text=t1,font=("Lucida Console",int(tamaño)))
                    im1.place(x=px,y=90)
                    im3 = Label(raiz,text="Imagen Original",font=("Lucida Console",10))
                    im3.place(x=px+30,y=90+alto)
                    px1 = ((300-ancho)/2)+340
                    im2 = Label(raiz,text=t2,font=("Lucida Console",int(tamaño)))
                    im2.place(x=px1,y=90)
                    im4 = Label(raiz,text="Eliminado",font=("Lucida Console",10))
                    im4.place(x=px+390,y=90+alto)   
                    windows.destroy()  
                    ventana.destroy()   
                else:
                    ventanaEmergente("Error numero de elementos excede tamaño de matriz")
            else:
                ventanaEmergente("Error numero de columnas excede tamaño de matriz ")
        else:
            ventanaEmergente("Error numero de filas excede tamaño de matriz ")
    else:
        ventanaEmergente("Error Ingrese solo Numero")


def guardar(ventana,windows,s1,s2,d1,d2,f,c,matriz):
    global x1,x2,y1,y2,filas,columnas,elementos
    auxiliar = copy.deepcopy(matriz)
    if s1.isdigit() and s2.isdigit() and d1.isdigit() and d2.isdigit():
        if int(s1) <= int(c) and int(s1) >= 1 :
            if int(s2) <= int(f) and int(s2) >= 1 :
                if int(d1) <= int(c) and int(d1) >= 1 :
                    if int(d2) <= int(f) and int(d2) >= 1 :
                        f1 = int(s1)
                        c1 = int(s2)
                        f2 = int(d1)
                        c2 = int(d2)
                        if f1 <= f2: #siguiente
                            if c1 <= c2: #abajo
                                aux = matriz.Search(f1,c1)
                                avanzax = c2-c1
                                avanzay = f2-f1
                                i = 0
                                j = 0
                                aun1 = aux
                                while j <= avanzay:
                                    aux = aun1
                                    while i <= avanzax:
                                        aux.dato = '-'
                                        aux = aux.siguiente
                                        i = i + 1
                                    j = j + 1
                                    i = 0
                                    aun1 = aun1.abajo
                            elif c1 > c2: #abajo
                                aux = matriz.Search(f2,c2)
                                avanzax = c1-c2
                                avanzay = f2-f1
                                i = 0
                                j = 0
                                aun1 = aux
                                while j <= avanzay:
                                    aux = aun1
                                    while i <= avanzax:
                                        aux.dato = '-'
                                        aux = aux.siguiente
                                        i = i + 1
                                    j = j + 1
                                    i = 0
                                    aun1 = aun1.arriba
                        elif f2 <= f1: #siguiente
                            if c1 <= c2: #abajo
                                aux = matriz.Search(f1,c1)
                                avanzax = c2-c1
                                avanzay = f1-f2
                                i = 0
                                j = 0
                                aun1 = aux
                                while j <= avanzay:
                                    aux = aun1
                                    while i <= avanzax:
                                        aux.dato = '-'
                                        aux = aux.siguiente
                                        i = i + 1
                                    j = j + 1
                                    i = 0
                                    aun1 = aun1.arriba
                            elif c1 > c2: #abajo
                                aux = matriz.Search(f2,c2)
                                avanzay = f1-f2
                                avanzax = c1-c2
                                i = 0
                                j = 0
                                aun1 = aux
                                while j <= avanzay:
                                    aux = aun1
                                    while i <= avanzax:
                                        aux.dato = '-'
                                        aux = aux.siguiente
                                        i = i + 1
                                    j = j + 1
                                    i = 0
                                    aun1 = aun1.abajo
                        tamaño = 25
                        t1 = auxiliar.Pintando()
                        t2 = matriz.Pintando()
                        ancho = 0.83*float(tamaño)*float(matriz.primero.c)
                        alto = 1.36*float(tamaño)*float(matriz.primero.f)
                        if alto >= 400 or ancho >= 300:
                            while alto>= 380 or ancho >= 300 :
                                tamaño = tamaño-0.3
                                alto = 1.36*float(tamaño)*float(matriz.primero.f)
                                ancho = 0.83*float(tamaño)*float(matriz.primero.c)      
                        px = (300-ancho)/2
                        im1 = Label(raiz,text=t1,font=("Lucida Console",int(tamaño)))
                        im1.place(x=px,y=90)
                        im3 = Label(raiz,text="Imagen Original",font=("Lucida Console",10))
                        im3.place(x=px+30,y=90+alto)
                        px1 = ((300-ancho)/2)+340
                        im2 = Label(raiz,text=t2,font=("Lucida Console",int(tamaño)))
                        im2.place(x=px1,y=90)
                        im4 = Label(raiz,text="Eliminado",font=("Lucida Console",10))
                        im4.place(x=px+390,y=90+alto)   
                        windows.destroy()  
                        ventana.destroy()
                    else:
                        ventanaEmergente("Error numero excede tamaño de matriz Y:2")
                else:
                    ventanaEmergente("Error numero excede tamaño de matriz X:2")
            else:
                ventanaEmergente("Error numero excede tamaño de matriz Y:1")
        else:
            ventanaEmergente("Error numero excede tamaño de matriz X:1")
    else:
        ventanaEmergente("Error Ingrese solo Numero")

def verImagen(combo):
    img = combo.get()
    if img == 'Seleccione Imagen':
        ventanaEmergente("Porfavor Seleccione una Imagen")
    else:
        tamaño = 25
        aux = listaImagenes.BuscarMatriz(img)
        matriz = aux.matriz
        imagen = Tk()
        imagen.title("Imagen")
        texto = matriz.Pintando()
        ancho = 0.83*float(tamaño)*float(matriz.primero.c)
        alto = 1.36*float(tamaño)*float(matriz.primero.f)
        if alto >= 700:
            while alto>= 700:
                tamaño = tamaño-0.3
                alto = 1.36*float(tamaño)*float(matriz.primero.f)       
        x_ventana = raiz.winfo_screenwidth() // 2 - int(ancho) // 2
        y_ventana = raiz.winfo_screenheight() // 2 - int(alto) // 2
        posicion = str(int(ancho)) + "x" + str(int(alto)) + "+" + str(x_ventana) + "+" + str(y_ventana)
        imagen.geometry(posicion)
        lb2 = ttk.Label(imagen,text=texto,font=("Lucida Console",int(tamaño)))
        lb2.place(x=0,y=0)
        imagen.mainloop()


       # limite = Label(windows,text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n",font=("Lucida Console",20)).place(x=345,y=20)
        #limite1 = Label(windows,text="-------------------------------------------------------------------",font=("Lucida Console",20)).place(x=0,y=30)

def operacion():
    aux = listaImagenes.primero



    print("hola")

                                      
raiz = Tk()
raiz.title("Principal")
ancho_ventana = 650
alto_ventana = 460
x_ventana = raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = raiz.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
raiz.geometry(posicion)
raiz.iconbitmap("codificacion.ico")
botonCargar = Button(raiz,text="Cargar Archivo",command=carga,height = 3,width=20)
botonCargar.place(x=10,y=20)
botonOperacion = Button(raiz,text="Operaciones",command=operacion,height = 3,width=20)
botonOperacion.place(x=170,y=20)
botonReporte = Button(raiz,text="Reporte",command=operaciones,height = 3,width=20)
botonReporte.place(x=330,y=20)
botonAyuda = Button(raiz,text="Ayuda",command=operaciones,height = 3,width=20)
botonAyuda.place(x=490,y=20)
raiz.mainloop()