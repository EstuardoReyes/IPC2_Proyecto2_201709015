from tkinter import Tk     
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
            matriz = Matriz(nombre)
            error = False
            while x < len(imagen):
                actual = imagen[x]
                if state == 0:
                    if ord(actual) == 10 or ord(actual) == 9:
                        x = x + 1
                    elif ord(actual) == 45 or ord(actual) == 42:
                        state = 1
############################################################################################################
                elif state == 1:
                    if ord(actual) == 45: # guion
                        x = x + 1
                        print(str(fi)+" "+str(colu))
                        matriz.Agregar(fi,colu,' ')                
                    elif ord(actual) == 42: # asterisco
                        x = x + 1
                        print(str(fi)+" "+str(colu))
                        matriz.Agregar(fi,colu,'▓')
                    else:
                        x = x + 1
                        fi = fi + 1
                        state = 0
                        colu = 0
                    colu = colu + 1
        #listaImagenes.Agregar(imagen)
          



                 

    
     
       

def graphi():
    if archivo_Seleccionado == False:
        print("Archivo de datos de entrada no seleccionado previamente")
    if procesar == False:
        print("Proceso de archivo de entrada no realizado previamente")
    else:
        print('Matrices Almacenadas')
        aux = listaCircular.get_Primero()
        head = listaCircular.get_Primero()
        salir = False
        salir2 = False
        listaNodo = []
        i=1
        while salir2 == False:
            while salir == False:
                print(str(i)+". "+aux.getDato().getNombre())
                i = i+1
                listaNodo.append(aux) 
                if (aux.siguiente != head):
                    aux = aux.siguiente
                else:
                    salir = True
            a = input("Seleccione 1 matriz: ")
            if int(a)<=i-1 and int(a)>=1:
                nodoUsar = listaNodo[int(a)-1]
                break
                #salir2 = True
            else:
                print("Seleccione una matriz entre las opciones")
        nom = nodoUsar.getDato().getNombre()
        g = Digraph('unix', filename='Reporte',node_attr={'color': 'lightblue2', 'style': 'filled'})
        g.edge('Matrices', nom)
        g.edge(nom, 'n='+nodoUsar.getDato().getFila())
        g.edge(nom, 'm='+nodoUsar.getDato().getColumna())
        matrizUsar = nodoUsar.getDato().getEntrada()
        for i in range(1,len(matrizUsar[0])):
            listaNumeros = []
            for j in range(1,len(matrizUsar)):
                listaNumeros.append(matrizUsar[j][i])
            g.edge(nom,"["+str(1)+","+str(i)+"] = "+str(listaNumeros[0]))
            for q in range(1,len(listaNumeros)):
                g.edge("["+str(q)+","+str(i)+"] = "+str(listaNumeros[q-1]),"["+str(q+1)+","+str(i)+"] = "+str(listaNumeros[q]))
        g.view()
                                        
carga()