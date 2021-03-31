from tkinter import *  
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

archivo_Seleccionado = False
salida = False
listaAlpha = []
listaImagenes = ListaDoble()
procesar = False

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
            
        listaImagenes.Agregar(matriz)
        print("Se agrego Imagen: "+nombre)
    
def ventana():
    raiz = Tk()
    raiz.title("Principal")
    raiz.geometry("650x480")
    raiz.iconbitmap("codificacion.ico")
    botonCargar = Button(raiz,text="Cargar Archivo",command=carga,height = 3,width=20).place(x=10,y=20)
    botonOperacion = Button(raiz,text="Operaciones",command=operaciones,height = 3,width=20).place(x=170,y=20)
    botonOperacion = Button(raiz,text="Reporte",command=operaciones,height = 3,width=20).place(x=330,y=20)
    botonOperacion = Button(raiz,text="Ayuda",command=operaciones,height = 3,width=20).place(x=490,y=20)
    aux = listaImagenes.primero
    if aux != None:
        texto = aux.Pintando()
        imagen1 = Label(raiz,text=texto).place(x=20,y=100)
    raiz.mainloop()
    

def operaciones():
    print("hola")

                                      
ventana()
ventana()