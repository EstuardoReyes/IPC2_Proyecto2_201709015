from tkinter import Tk,Button,Label,Entry
from tkinter import ttk
import copy
import webbrowser
import time
import subprocess
from tkinter.colorchooser import askcolor
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
log = []
listaImagenes = ListaDoble()
procesar = False
x1 = 0
y1 = 0
x2 = 0
y2 = 0
elementos = 0
filas = 0
columnas = 0

def reporte():
    mensaje =  """<!doctype html>
                        <html>
                        <head>
                        <title>REPORTE</title>
                        <link href="CSS\pa.css" rel="stylesheet" type="text/css">
                        </head>
                        <body>
                        <div class="container"> 
                        <header> <a href="">
                        <h6 class="logo">REPORTE</h6>
                        </a>
                        </header>
                        <section class="hero" id="hero">
                        <h3 class="hero_header">REPORTE</h3>
                       
                        </section>
                        <section class="banner">
                        """
    i = 1
    tamaño = 20
    for lo in log:    
        mensaje = mensaje + """ <h4><font color = "white">"""+lo+"""</font></h4>"""
        i = i + 1
        tamaño = tamaño + 38
    mens =""" <div class="copyright">&copy;2020- <strong>Edwin estuardo reyes reyes</strong></div>
                        </div>
                        </body>
                        </html>"""
    mensaje = mensaje + mens


    css = """@charset "UTF-8";
                    /* Body */
                    html {
                            font-size: 30px;
                        }
                        body {
                            font-family: source-sans-pro;
                            background-color: #f2f2f2;
                            margin-top: 0px;
                            margin-right: 0px;
                            margin-bottom: 0px;
                            margin-left: 0px;
                            font-style: normal;
                            font-weight: 200;
                            }
                            .container {
                            width: 70%;
                            margin-left: auto;
                            margin-right: auto;
                            height: 700px;
                                        }
                            header {
                            width: 100%;
                            height: 8%;
                            background-color: #52bad5;
                            border-bottom: 1px solid #2C9AB7;
                            }
                            .logo {
                        color: #fff;
                            font-weight: bold;
                            text-align: undefined;
                            width: 10%;
                            float: left;
                            margin-top: 15px;
                            margin-left: 25px;
                            letter-spacing: 4px;
                                }
                            .hero_header {
                            color: #FFFFFF;
                            text-align: center;
                            margin-top: 0px;
                            margin-right: 0px;
                            margin-bottom: 0px;
                            margin-left: 0px;
                            letter-spacing: 4px;
                                }
                            .hero {
                            background-color: #B3B3B3;
                            padding-top: 100px;
                            padding-bottom: 80px;
                            }
                            .light {
                                font-weight: bold;
                                color: #717070;
                            }
                            .tagline {
                                text-align: center;
                                color: #FFFFFF;
                                margin-top: 4px;
                                font-weight: lighter;
                                text-transform: uppercase;
                                letter-spacing: 1px;
                            }

                            .banner {
                                background-color: #2D9AB7;
                                background-image: url(../images/parallax.png);
                                +height:"""+str(tamaño)+"""px;
                                background-attachment: fixed;
                                background-size: cover;
                                background-repeat: no-repeat;
                            }
                            .parallaxx {
                                color: #FFFFFF;
                                text-align: left;
                                padding-left: 200px;
                                padding-right: 100px;
                                padding-top: 50px;
                                letter-spacing: 2px;
                                margin-top: 0px;
                                margin-bottom: 0px
                            }
                            .parallax {
                                color: #FFFFFF;
                                text-align: left;
                                padding-left: 200px;
                                padding-right: 100px;
                                padding-top: 10px;
                                letter-spacing: 2px;
                                margin-top: 0px;
                                margin-bottom: 0px
                            }

                            .paralla {
                                color: #ffffff5e;
                                text-align: left;
                                padding-left: 200px;
                                padding-right: 100px;
                                padding-top: 10px;
                                letter-spacing: 2px;
                                margin-top: 0px;
                                margin-bottom: 0px
                            }


                            .copyright {
                                text-align: center;
                                padding-top: 20px;
                                padding-bottom: 20px;
                                background-color: #717070;
                                color: #ffffff;
                                text-transform: uppercase;
                                font-weight: lighter;
                                letter-spacing: 2px;
                                border-top-width: 2px;
                            }
                            """
    if os.path.exists("CSS") == False :
        os.makedirs("CSS")
    g = open("CSS\pa.css",'wb')
    g.write(bytes(css,"ascii"))
    g.close()
    f = open('Reporte.html','wb')
    f.write(bytes(mensaje,"ascii"))
    f.close()
    webbrowser.open_new_tab('Reporte.html')


def carga():
    root = Tk()
    root.withdraw()
    root.wm_attributes("-topmost", 1)
    archivo = askopenfilename(filetypes =(("Archivo TXT", "*.txt"),("Todos Los Archivos","*.*")),title = "Busque su archivo.")
    root.update()
    root.destroy()
    xmldoc = xml.dom.minidom.parse(archivo)
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
            llena = 0
            vacia = 0
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
                            vacia = vacia + 1           
                    elif ord(actual) == 42: # asterisco
                        x = x + 1
                        if fi>int(fila) or colu>int(columna):
                            print("Error Matriz mayor que establecida")
                        else:
                            matriz.Agregar(fi,colu,'*')       
                            llena = llena + 1  
                    else:
                        fi = fi + 1
                        state = 0
                        colu = 0
                    colu = colu + 1
        Nodo = NodoLista(matriz,nombre,fila,columna)  
        listaImagenes.Agregar(Nodo)
        texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ nombre+" - Espacio lleno: "+str(llena)+" - Espacio vacio: "+str(vacia)
        log.append(texto)
        print("Se agrego Imagen: "+nombre)

def ventanaEmergente(texto): 
    messagebox.showinfo(message=texto, title="Avisos")

def close_window(objeto):
    objeto.destroy()

def operaciones():
    if listaImagenes.primero == None :
        ventanaEmergente("Porfavor Seleccione Carga Primero")
    else:
        tamaño = 17
        windows = Tk()
        windows['bg'] = '#B3B3B3'
        windows.title("Operaciones Validas")
        ancho_ventana = 700
        alto_ventana = 400
        x_ventana = raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
        y_ventana = raiz.winfo_screenheight() // 2 - alto_ventana // 2
        posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
        windows.geometry(posicion)
        Lb1 = Label(windows,text="Imagenes Existentes: ",bg="#B3B3B3",font=("Lucida Console",15))
        Lb1.place(x=60,y=30)
        combo = ttk.Combobox(windows,font=("Lucida Console",13))
        combo.place(x=320,y=30)
        opciones = ['Seleccione Imagen']
        aux = listaImagenes.primero
        while aux != None:
            opciones.append(aux.nombre)
            aux = aux.siguiente
        combo['values']=opciones
        combo.current(0)
        windows.iconbitmap("codificacion.ico")
        button = Button(windows, text="ver",command = lambda: verImagen(combo),bg = "#2D9AB7",fg = "#FFFFFF",font=("Lucida Console",15))
        button.place(x=560,y=20)

        combo1 = ttk.Combobox(windows,font=("Lucida Console",13))
        combo1.place(x=50,y=170)
        opc = ['Seleccione Opcion','1. Rotacion Horizontal','2. Rotacion Vertical','3. Transpuesta','4. Limpiar Zona','5. Agregar Linea Horizontal','6. Agregar Linea Vertical','7. Agregar Rectangulo','8. Agregar Triangulo Rectangular']
        combo1['values']=opc
        combo1.current(0)
        i = Label(windows,text="Operaciones con 1 Imagen",bg="#B3B3B3",font=("Lucida Console",15))
        i.place(x=20,y=100)
        combo2 = ttk.Combobox(windows,font=("Lucida Console",13))
        combo2.place(x=50,y=220)
        opcione = ['Seleccione Imagen']
        aux = listaImagenes.primero
        while aux != None:
            opcione.append(aux.nombre)
            aux = aux.siguiente
        combo2['values']=opcione
        combo2.current(0)
        ii = Label(windows,text="Operaciones con 2 Imagenes",bg="#B3B3B3",font=("Lucida Console",15))
        ii.place(x=350,y=100)
        b1 = Button(windows,text="Calcular",command = lambda: operacion1(combo1,combo2,windows),bg = "#2D9AB7",fg = "#FFFFFF",font=("Lucida Console",15))
        b1.place(x=100,y=280)

        combo5 = ttk.Combobox(windows,font=("Lucida Console",13))
        combo5.place(x=440,y=170)
        opc = ['Seleccione 1. Imagen']
        aux = listaImagenes.primero
        while aux != None:
            opc.append(aux.nombre)
            aux = aux.siguiente
        combo5['values']=opc
        combo5.current(0)
        combo6 = ttk.Combobox(windows,font=("Lucida Console",13))
        combo6.place(x=440,y=220)
        opcione = ['Seleccione 2. Imagen']
        aux = listaImagenes.primero
        while aux != None:
            opcione.append(aux.nombre)
            aux = aux.siguiente
        combo6['values']=opcione
        combo6.current(0)
        combo7 = ttk.Combobox(windows,font=("Lucida Console",13))
        combo7.place(x=440,y=270)
        opcione = ['Seleccione Opcion','1. Union','2. Interseccion','3. Diferencia','4. Diferencia Simetrica']
        aux = listaImagenes.primero
        combo7['values']=opcione
        combo7.current(0)
        b1 = Button(windows,text="Calcular",command = lambda: operacion2(combo5,combo6,combo7,windows),bg = "#2D9AB7",fg = "#FFFFFF",font=("Lucida Console",15))
        b1.place(x=480,y=320)
        windows.mainloop()
        
def operacion2(combo1,combo2,combo3,ventana):
    img1 = combo1.get()
    img2 = combo2.get()
    opcion = combo3.get()
    if img1 == 'Seleccione 1. Imagen':
        ventanaEmergente("Porfavor Seleccione primera imagen Valida")
    elif img2 == 'Seleccione 2. Imagen':
        ventanaEmergente("Porfavor Seleccione segunda imagen Valida")
    elif opcion == 'Seleccione Opcion':
        ventanaEmergente("Porfavor Seleccione Opcion Primero")
    else:
        ima1 = listaImagenes.BuscarMatriz(img1) # Nodo que cuenta con la matriz de aqui tengo que remplazar
        ima2 = listaImagenes.BuscarMatriz(img2)
        if opcion == '1. Union':
            newMatriz = Matriz("g",100,100)
            aux1 = ima1.matriz.primero.fila.primero.Nodo
            aux2 = ima2.matriz.primero.fila.primero.Nodo
            c = 1
            f = 1
            texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Operacion: Union - Matrices Usadas: "+ima1.matriz.primero.nombre+" y "+ ima2.matriz.primero.nombre
            log.append(texto)
            while aux1 != None or aux2 != None:
                fila1 = aux1
                fila2 = aux2
                while fila1 != None or fila2 != None:
                    if fila1 != None or fila2 != None:
                        if fila1  != None and fila1.dato == '*':
                            newMatriz.Agregar(f,c,'*')
                        elif fila2 != None and fila2.dato == '*':
                            newMatriz.Agregar(f,c,'*')
                        else:
                            newMatriz.Agregar(f,c,'-')
                    if fila1 != None:
                        fila1 = fila1.siguiente
                    if fila2 != None:
                        fila2 = fila2.siguiente
                    c = c + 1
                if aux1 != None:
                    aux1 = aux1.abajo
                if aux2 != None:
                    aux2 = aux2.abajo
                c = 1
                f = f + 1
        elif opcion == '2. Interseccion':
            newMatriz = Matriz("g",100,100)
            aux1 = ima1.matriz.primero.fila.primero.Nodo
            aux2 = ima2.matriz.primero.fila.primero.Nodo
            texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Operacion: Interseccion - Matrices Usadas: "+ima1.matriz.primero.nombre+" y "+ ima2.matriz.primero.nombre
            log.append(texto)
            c = 1
            f = 1
            while aux1 != None or aux2 != None:
                fila1 = aux1
                fila2 = aux2
                while fila1 != None or fila2 != None:
                    if fila1 != None or fila2 != None:
                        if fila1  != None and fila1.dato == '*':
                            if fila2 != None and fila2.dato == '*':
                                newMatriz.Agregar(f,c,'*')
                            else:
                                newMatriz.Agregar(f,c,'-')
                        else:
                            newMatriz.Agregar(f,c,'-')
                    if fila1 != None:
                        fila1 = fila1.siguiente
                    if fila2 != None:
                        fila2 = fila2.siguiente
                    c = c + 1
                if aux1 != None:
                    aux1 = aux1.abajo
                if aux2 != None:
                    aux2 = aux2.abajo
                c = 1
                f = f + 1
        elif opcion == '3. Diferencia':
            newMatriz = Matriz("g",100,100)
            aux1 = ima1.matriz.primero.fila.primero.Nodo
            aux2 = ima2.matriz.primero.fila.primero.Nodo
            c = 1
            f = 1
            texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Operacion: Diferencia - Matrices Usadas: "+ima1.matriz.primero.nombre+" y "+ ima2.matriz.primero.nombre
            log.append(texto)
            while aux1 != None or aux2 != None:
                fila1 = aux1
                fila2 = aux2
                while fila1 != None or fila2 != None:
                    if fila1 != None or fila2 != None:
                        if fila1  != None and fila1.dato == '*':
                            if fila2 != None and fila2.dato == '-':
                                newMatriz.Agregar(f,c,'*')
                            elif fila2 == None:
                                newMatriz.Agregar(f,c,'*')
                            else:
                                newMatriz.Agregar(f,c,'-')
                        else:
                            newMatriz.Agregar(f,c,'-')
                    if fila1 != None:
                        fila1 = fila1.siguiente
                    if fila2 != None:
                        fila2 = fila2.siguiente
                    c = c + 1
                if aux1 != None:
                    aux1 = aux1.abajo
                if aux2 != None:
                    aux2 = aux2.abajo
                c = 1
                f = f + 1
        elif opcion == '4. Diferencia Simetrica':
            newMatriz = Matriz("g",100,100)
            aux1 = ima1.matriz.primero.fila.primero.Nodo
            aux2 = ima2.matriz.primero.fila.primero.Nodo
            c = 1
            f = 1
            texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Operacion: Diferencia Simetrica - Matrices Usadas: "+ima1.matriz.primero.nombre+" y "+ ima2.matriz.primero.nombre
            log.append(texto)
            while aux1 != None or aux2 != None:
                fila1 = aux1
                fila2 = aux2
                while fila1 != None or fila2 != None:
                    if fila1 != None or fila2 != None:
                        if fila1  != None and fila1.dato == '*':
                            if fila2 != None and fila2.dato == '-':
                                newMatriz.Agregar(f,c,'*')
                            elif fila2 == None:
                                newMatriz.Agregar(f,c,'*')
                            else:
                                newMatriz.Agregar(f,c,'-')
                        elif fila2  != None and fila2.dato == '*':
                            if fila1 != None and fila1.dato == '-':
                                newMatriz.Agregar(f,c,'*')
                            elif fila1 == None:
                                newMatriz.Agregar(f,c,'*')
                            else:
                                newMatriz.Agregar(f,c,'-')
                        else:
                            newMatriz.Agregar(f,c,'-')
                    if fila1 != None:
                        fila1 = fila1.siguiente
                    if fila2 != None:
                        fila2 = fila2.siguiente
                    c = c + 1
                if aux1 != None:
                    aux1 = aux1.abajo
                if aux2 != None:
                    aux2 = aux2.abajo
                c = 1
                f = f + 1


        newMatriz.primero.f = f
        newMatriz.primero.c = c
        vent = Tk()
        vent.title("Ingreso de Datos")
        ancho = 460
        alto = 270     
        x_ventana = raiz.winfo_screenwidth() // 2 - int(ancho) // 2
        y_ventana = raiz.winfo_screenheight() // 2 - int(alto) // 2
        posicion = str(int(ancho)) + "x" + str(int(alto)) + "+" + str(x_ventana) + "+" + str(y_ventana)
        vent.geometry(posicion)
        lb = ttk.Label(vent,text="Operacion Realizada Exitosamente!",font=("Lucida Console",14))
        lb.place(x=33,y=10)
        lb1 = ttk.Label(vent,text="Agregar Matriz : Ingrese nombre",font=("Lucida Console",10))
        lb1.place(x=10,y=60)
        entry1 = ttk.Entry(vent)
        entry1.place(x=275,y=60)
        b1 = ttk.Button(vent,text="Agregar Matriz",command = lambda: agregar(ventana,vent,entry1.get(),newMatriz,f,c,ima1.matriz,ima2.matriz))
        b1.place(x=165,y=105)
        lb1 = ttk.Label(vent,text="Sustituir Matriz : Escoja Nombre",font=("Lucida Console",10))
        lb1.place(x=10,y=160)
        combo6 = ttk.Combobox(vent,font=("Lucida Console",13))
        combo6.place(x=290,y=160)
        opcione = ['Seleccione Imagen']
        aux = listaImagenes.primero
        while aux != None:
            opcione.append(aux.nombre)
            aux = aux.siguiente
        combo6['values']=opcione
        combo6.current(0)
        b2 = ttk.Button(vent,text="Sustituir Matriz",command = lambda: sustituir(ventana,vent,newMatriz,f,c,combo6.get(),ima1.matriz,ima2.matriz))
        b2.place(x=165,y=205)
        vent.mainloop()
        
def sustituir(ventana,vent,matriz,f,c,nombre,im1,im2):
    matri = listaImagenes.BuscarMatriz(nombre)
    matri.matriz = matriz
    resultante = matriz.Pintando()
    imagen1 = im1.Pintando()
    imagen2 = im2.Pintando()
    tamaño = 25
    tamaño1 = 25
    tamaño2 = 25
    anchoResultante = 0.83*float(tamaño)*float(matriz.primero.c)
    altoResultante = 1.36*float(tamaño)*float(matriz.primero.f)
    if altoResultante >= 400 or anchoResultante >= 200:
        while altoResultante>= 380 and anchoResultante >= 200 :
            tamaño1 = tamaño1-0.3
            altoResultante = 1.36*float(tamaño)*float(matriz.primero.f)
            anchoResultante = 0.83*float(tamaño)*float(matriz.primero.c) 
    anchoIma1 = 0.83*float(tamaño1)*float(im1.primero.c)
    altoIma1 = 1.36*float(tamaño1)*float(im1.primero.f)
    if altoIma1 >= 400 or anchoIma1 >= 200:  
        while altoIma1>= 380 and anchoIma1 >= 200 :
            tamaño1 = tamaño1-0.3
            altoIma1 = 1.36*float(tamaño1)*float(im1.primero.f)
            anchoIma1 = 0.83*float(tamaño1)*float(im1.primero.c)
    anchoIma2 = 0.83*float(tamaño2)*float(im2.primero.c)
    altoIma2 = 1.36*float(tamaño2)*float(im2.primero.f)
    if altoIma2 >= 400 or anchoIma2 >= 200:  
        while altoIma2>= 380 and anchoIma2 >= 200 :
            tamaño2 = tamaño2-0.3
            altoIma2 = 1.36*float(tamaño2)*float(im2.primero.f)
            anchoIma2 = 0.83*float(tamaño2)*float(im2.primero.c)    
    px = (210-anchoIma1)/2+5
    im1 = Label(raiz,text=imagen1,font=("Lucida Console",int(tamaño1)))
    im1.place(x=px,y=90)
    im3 = Label(raiz,text="1ra. Imagen",font=("Lucida Console",10))
    im3.place(x=px+40,y=90+altoIma1)
    px1 = ((210-anchoIma2)/2)+220
    im2 = Label(raiz,text=imagen2,font=("Lucida Console",int(tamaño2)))
    im2.place(x=px1,y=90)
    im4 = Label(raiz,text="2da. Imagen",font=("Lucida Console",10))
    im4.place(x=px1+40,y=90+altoIma2)
    px2 = ((210-anchoResultante)/2)+350
    im2 = Label(raiz,text=resultante,font=("Lucida Console",int(tamaño)))
    im2.place(x=px2,y=90)
    im4 = Label(raiz,text="Resultado",font=("Lucida Console",10))
    im4.place(x=px2+50,y=40+altoResultante)
    ventana.destroy()
    vent.destroy()

def agregar(ventana,vent,c1,matriz,f,c,im1,im2):
    Nodo = NodoLista(matriz,c1,f,c)  
    listaImagenes.Agregar(Nodo)
    resultante = matriz.Pintando()
    imagen1 = im1.Pintando()
    imagen2 = im2.Pintando()
    tamaño = 25
    tamaño1 = 25
    tamaño2 = 25
    anchoResultante = 0.83*float(tamaño)*float(matriz.primero.c)
    altoResultante = 1.36*float(tamaño)*float(matriz.primero.f)
    if altoResultante >= 400 or anchoResultante >= 200:
        while altoResultante>= 380 and anchoResultante >= 200 :
            tamaño1 = tamaño1-0.3
            altoResultante = 1.36*float(tamaño)*float(matriz.primero.f)
            anchoResultante = 0.83*float(tamaño)*float(matriz.primero.c) 
    anchoIma1 = 0.83*float(tamaño1)*float(im1.primero.c)
    altoIma1 = 1.36*float(tamaño1)*float(im1.primero.f)
    if altoIma1 >= 400 or anchoIma1 >= 200:  
        while altoIma1>= 380 and anchoIma1 >= 200 :
            tamaño1 = tamaño1-0.3
            altoIma1 = 1.36*float(tamaño1)*float(im1.primero.f)
            anchoIma1 = 0.83*float(tamaño1)*float(im1.primero.c)
    anchoIma2 = 0.83*float(tamaño2)*float(im2.primero.c)
    altoIma2 = 1.36*float(tamaño2)*float(im2.primero.f)
    if altoIma2 >= 400 or anchoIma2 >= 200:  
        while altoIma2>= 380 and anchoIma2 >= 200 :
            tamaño2 = tamaño2-0.3
            altoIma2 = 1.36*float(tamaño2)*float(im2.primero.f)
            anchoIma2 = 0.83*float(tamaño2)*float(im2.primero.c)    
    px = (210-anchoIma1)/2+5
    im1 = Label(raiz,text=imagen1,font=("Lucida Console",int(tamaño1)))
    im1.place(x=px,y=90)
    im3 = Label(raiz,text="1ra. Imagen",font=("Lucida Console",10))
    im3.place(x=px+30,y=90+altoIma1)
    px1 = ((210-anchoIma2)/2)+220
    im2 = Label(raiz,text=imagen2,font=("Lucida Console",int(tamaño2)))
    im2.place(x=px1,y=90)
    im4 = Label(raiz,text="2da. Imagen",font=("Lucida Console",10))
    im4.place(x=px1+15,y=90+altoIma2)
    px2 = ((210-anchoResultante)/2)+350
    im2 = Label(raiz,text=resultante,font=("Lucida Console",int(tamaño)))
    im2.place(x=px2,y=90)
    im4 = Label(raiz,text="Resultado",font=("Lucida Console",10))
    im4.place(x=px2+15,y=100+altoResultante)
    ventana.destroy()
    vent.destroy()

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
            im1 = Label(raiz,text=t1,font=("Lucida Console",int(tamaño)),bg = "#B3B3B3")
            im1.place(x=px,y=90)
            im3 = Label(raiz,text="Imagen Original",font=("Lucida Console",13),bg = "#2D9AB7",fg = "#FFFFFF")
            im3.place(x=px+25,y=90+alto)
            px1 = ((300-ancho)/2)+340
            im2 = Label(raiz,text=t2,font=("Lucida Console",int(tamaño)),bg = "#2D9AB7",fg = "#FFFFFF")
            im2.place(x=px1,y=90)
            im4 = Label(raiz,text="Rotacion Horizontal",font=("Lucida Console",13),bg = "#2D9AB7",fg = "#FFFFFF")
            im4.place(x=px+360,y=90+alto)
            texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Operacion: Rotacion Horizontal - Matriz Usada: "+matriz.primero.nombre
            log.append(texto)
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
            texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Operacion: Rotacion Vertical - Matriz Usada: "+matriz.primero.nombre
            log.append(texto)
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
            texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Operacion: Transpuesta - Matriz Usada: "+matriz.primero.nombre
            log.append(texto)
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
        elif cb == '6. Agregar Linea Vertical':
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
            bo = ttk.Button(vent,text="Aceptar",command = lambda: agregarV(ventana,vent,entry1.get(),entry2.get(),entry3.get(),matriz.primero.f,matriz.primero.c,matriz))
            bo.place(x=140,y=200)
        elif cb == '7. Agregar Rectangulo':
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
            bo = ttk.Button(vent,text="Aceptar",command = lambda: guardarA(ventana,vent,entry1.get(),entry2.get(),entry3.get(),entry4.get(),matriz.primero.f,matriz.primero.c,matriz))
            bo.place(x=140,y=200)
        elif cb == '8. Agregar Triangulo Rectangular':
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
            bo = ttk.Button(vent,text="Aceptar",command = lambda: guardarv(ventana,vent,entry1.get(),entry2.get(),entry3.get(),matriz.primero.f,matriz.primero.c,matriz))
            bo.place(x=140,y=200)

def guardarv(ventana,windows,s1,s2,d1,f,c,matriz):
    global x1,x2,y1,y2,filas,columnas,elementos
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
                    j = 0
                    t = 1
                    aun1 = aux
                    if c1+elementos <= (int(c)+1) and f1+elementos <= (int(f)+1):
                        while j < elementos:
                            aux = aun1
                            while i < t:
                                aux.dato = '*'
                                aux = aux.siguiente
                                i = i + 1
                            j = j + 1
                            i = 0
                            t = t + 1
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
                        im4 = Label(raiz,text="Triangulo Rectangulo",font=("Lucida Console",10))
                        im4.place(x=px+390,y=90+alto)   
                        windows.destroy()  
                        ventana.destroy()
                        texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Operacion: Agregar Triangulo Rectangulo - Matriz Usada: "+matriz.primero.nombre
                        log.append(texto)
                    else:
                        texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Espacio no disponible - Operacion : Agregar Triangulo Rectangulo - Matriz Usada: "+matriz.primero.nombre
                        log.append(texto)
                        ventanaEmergente("Error Espacio no disponible")
                else:
                    texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Excede tamaño de matriz - Operacion : Agregar Triangulo Rectangulo - Matriz Usada: "+matriz.primero.nombre
                    log.append(texto)
                    ventanaEmergente("Error numero excede tamaño de matriz")
            else:
                texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Excede numero de tamaño de matriz - Operacion : Agregar Triangulo Rectangulo - Matriz Usada: "+matriz.primero.nombre
                log.append(texto)
                ventanaEmergente("Error numero excede tamaño de matriz c:1")
        else:
            texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Excede numero de tamaño de matriz - Operacion : Agregar Triangulo Rectangulo - Matriz Usada: "+matriz.primero.nombre
            log.append(texto)
            ventanaEmergente("Error numero excede tamaño de matriz f:1")
    else:
        ventanaEmergente("Error Ingrese solo Numero")
        texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Ingrese solo numeros - Operacion : Agregar Triangulo Rectangulo - Matriz Usada: "+matriz.primero.nombre
        log.append(texto)

def agregarV(ventana,windows,s1,s2,d1,f,c,matriz):
    auxiliar = copy.deepcopy(matriz)
    if s1.isdigit() and s2.isdigit() and d1.isdigit():
        if int(s1) <= int(c) and int(s1) >= 1 :
            if int(s2) <= int(f) and int(s2) >= 1 :
                if int(d1) <= int(f) and int(d1) >= 1 :
                    f1 = int(s1)
                    c1 = int(s2)
                    elementos = int(d1)
                    aux = matriz.Search(f1,c1)
                    i = 0
                    if f1+elementos <= int(f)+1:
                        while i < elementos:
                            aux.dato = '*'
                            i = i + 1
                            aux = aux.abajo
                    elif f1-elementos >= 0:
                        while i < elementos:
                            aux.dato = '*'
                            i = i + 1
                            aux = aux.arriba
                    else:
                        texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Operacion: Elementos no cabe en matriz - Matriz Usada: "+matriz.primero.nombre
                        log.append(texto)
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
                    im4 = Label(raiz,text="Agregar Linea Vertical",font=("Lucida Console",10))
                    im4.place(x=px+390,y=90+alto)   
                    windows.destroy()  
                    ventana.destroy()   
                    texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Operacion: Agregar Linea Vertical - Matriz Usada: "+matriz.primero.nombre
                    log.append(texto)
                else:
                    texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Excede tamaño de Matriz - Operacion : Agregar Linea Vertical - Matriz Usada: "+matriz.primero.nombre
                    log.append(texto)
                    ventanaEmergente("Error 1numero de elementos excede tamaño de matriz")
            else:
                texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Excede tamaño de Matriz - Operacion : Agregar Linea Vertical - Matriz Usada: "+matriz.primero.nombre
                log.append(texto)
                ventanaEmergente("Error numero de columnas excede tamaño de matriz ")
        else:
            texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Excede tamaño de Matriz - Operacion : Agregar Linea Vertical - Matriz Usada: "+matriz.primero.nombre
            log.append(texto)
            ventanaEmergente("Error numero de filas excede tamaño de matriz ")
    else:
        texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Ingrese solo Numeros - Operacion : Agregar Linea Vertical - Matriz Usada: "+matriz.primero.nombre
        log.append(texto)
        ventanaEmergente("Error Ingrese solo Numero")

def guardarA(ventana,windows,s1,s2,d1,d2,f,c,matriz):
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
                                        aux.dato = '*'
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
                                        aux.dato = '*'
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
                                        aux.dato = '*'
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
                                        aux.dato = '*'
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
                        im4 = Label(raiz,text="Rectangulo",font=("Lucida Console",10))
                        im4.place(x=px+390,y=90+alto)   
                        windows.destroy()  
                        ventana.destroy()
                        texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Operacion: Agregar Rectangulo - Matriz Usada: "+matriz.primero.nombre
                        log.append(texto)
                    else:
                        texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Excede tamaño de Matriz - Operacion : Añadir Rectangulo - Matriz Usada: "+matriz.primero.nombre
                        log.append(texto)
                        ventanaEmergente("Error numero excede tamaño de matriz c:2")
                else:
                    texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Excede tamaño de Matriz - Operacion : Añadir Rectangulo - Matriz Usada: "+matriz.primero.nombre
                    log.append(texto)
                    ventanaEmergente("Error numero excede tamaño de matriz f:2")
            else:
                texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Excede tamaño de Matriz - Operacion : Añadir Rectangulo - Matriz Usada: "+matriz.primero.nombre
                log.append(texto)
                ventanaEmergente("Error numero excede tamaño de matriz c:1")
        else:
            texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Excede tamaño de Matriz - Operacion : Añadir Rectangulo - Matriz Usada: "+matriz.primero.nombre
            log.append(texto)
            ventanaEmergente("Error numero excede tamaño de matriz f:1")
    else:
        texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Solo tiene que añadir numeros - Operacion : Añadir Rectangulo - Matriz Usada: "+matriz.primero.nombre
        log.append(texto)
        ventanaEmergente("Error Ingrese solo Numero")

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
                    if c1+elementos <= int(c)+1:
                        while i < elementos:
                            aux.dato = '*'
                            i = i + 1
                            aux = aux.siguiente
                    elif c1-elementos<=0:
                        while i < elementos:
                            aux.dato = '*'
                            i = i + 1
                            aux = aux.atras
                    else:
                        ventanaEmergente("Elementos no cabe en matriz")
                        texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Elementos no cabe en matriz - Operacion : Agregar Linea Horizontal - Matriz Usada: "+matriz.primero.nombre
                        log.append(texto)
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
                    im4 = Label(raiz,text="Agregar Linea Horinzontal",font=("Lucida Console",10))
                    im4.place(x=px+390,y=90+alto)   
                    windows.destroy()  
                    ventana.destroy() 
                    texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Operacion: Agregar linea Horizontal - Matriz Usada: "+matriz.primero.nombre
                    log.append(texto)  
                else:
                    texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Excede tamaño de Matriz - Operacion : Agregar Linea Horizontal - Matriz Usada: "+matriz.primero.nombre
                    log.append(texto)
                    ventanaEmergente("Error numero de elementos excede tamaño de matriz")
            else:
                texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Excede tamaño de Matriz - Operacion : Agregar Linea Horizontal - Matriz Usada: "+matriz.primero.nombre
                log.append(texto)
                ventanaEmergente("Error numero de columnas excede tamaño de matriz ")
        else:
            texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Excede tamaño de Matriz - Operacion : Agregar Linea Horizontal - Matriz Usada: "+matriz.primero.nombre
            log.append(texto)
            ventanaEmergente("Error numero de filas excede tamaño de matriz ")
    else:
        texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Ingrese solo numeros - Operacion : Agregar Linea Horizontal - Matriz Usada: "+matriz.primero.nombre
        log.append(texto)
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
                        texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Operacion: Limpiar Zona - Matriz Usada: "+matriz.primero.nombre
                        log.append(texto)
                        windows.destroy()  
                        ventana.destroy()
                    else:
                        texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Excede tamaño de Matriz - Operacion : Limpiar Zona - Matriz Usada: "+matriz.primero.nombre
                        log.append(texto)
                        ventanaEmergente("Error numero excede tamaño de matriz Y:2")
                else:
                    texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Excede tamaño de Matriz - Operacion : Limpiar Zona - Matriz Usada: "+matriz.primero.nombre
                    log.append(texto)
                    ventanaEmergente("Error numero excede tamaño de matriz X:2")
            else:
                texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Excede tamaño de Matriz - Operacion : Limpiar Zona - Matriz Usada: "+matriz.primero.nombre
                log.append(texto)
                ventanaEmergente("Error numero excede tamaño de matriz Y:1")
        else:
            texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Excede tamaño de Matriz - Operacion : Limpiar Zona - Matriz Usada: "+matriz.primero.nombre
            log.append(texto)
            ventanaEmergente("Error numero excede tamaño de matriz X:1")
    else:
        texto = time.strftime('%Y/%m/%d - %H:%M:%S', time.localtime())+" - "+ "Error: Solo Numeros - Operacion : Limpiar Zona - Matriz Usada: "+matriz.primero.nombre
        log.append(texto)
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
        imagen.configure(bg="#2D9AB7")
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
        lb2 = Label(imagen,text=texto,fg="#FFFFFF",bg="#2D9AB7",font=("Lucida Console",int(tamaño)))
        lb2.place(x=0,y=0)
        imagen.mainloop()


       # limite = Label(windows,text="|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n|\n",font=("Lucida Console",20)).place(x=345,y=20)
        #limite1 = Label(windows,text="-------------------------------------------------------------------",font=("Lucida Console",20)).place(x=0,y=30)

def documento():
    path = 'ensayo.pdf'
    subprocess.Popen([path], shell=True)
def ayuda():
    ayuda = Tk()
    ayuda.title("Ayuda")
    ancho_ventana = 403
    alto_ventana = 160
    ayuda.configure(bg="#B3B3B3")
    x_ventana = raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = raiz.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    ayuda.geometry(posicion)
    b1 = Button(ayuda,text="Datos del Desarrollador",command=datos,bg = "#2D9AB7",fg = "#FFFFFF",font=("Lucida Console",17))
    b1.place(x=30,y=30)
    b2 = Button(ayuda,text="Documentacion",command=documento,bg = "#2D9AB7",fg = "#FFFFFF",font=("Lucida Console",17))
    b2.place(x=100,y=90)
    ayuda.mainloop()

def datos():
    dato = Tk()
    dato.title("Datos del desarrolador")
    tk = Label(dato,text="Edwin Estuardo Reyes Reyes \n201709015\n 4to Semestre  ",bg = "#2D9AB7",fg = "#FFFFFF",font=("Lucida Console",17))
    tk.place(x=10,y=30)
    ancho_ventana = 390
    alto_ventana = 120
    dato.configure(bg="#2D9AB7")
    x_ventana = raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
    y_ventana = raiz.winfo_screenheight() // 2 - alto_ventana // 2
    posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
    dato.geometry(posicion)
    
def graphi():
    g = Digraph('unix', filename='Imagenes Cargadas en sistema',node_attr={'color': 'lightblue2', 'style': 'filled'})
    aux = listaImagenes.primero
    texto = "nombre "+aux.nombre+" fila "+aux.fila+" columna "+aux.columna
    g.edge('Lista de Imagenes',texto)
 
    while aux.siguiente != None:
        g.edge("nombre "+aux.nombre+" fila "+aux.fila+" columna "+aux.columna,"nombre "+aux.siguiente.nombre+" fila "+aux.siguiente.fila+" columna "+aux.siguiente.columna)
        aux = aux.siguiente
    g.view()

raiz = Tk()
raiz.title("Principal")
ancho_ventana = 650
alto_ventana = 460
raiz['bg'] = '#B3B3B3'
x_ventana = raiz.winfo_screenwidth() // 2 - ancho_ventana // 2
y_ventana = raiz.winfo_screenheight() // 2 - alto_ventana // 2
posicion = str(ancho_ventana) + "x" + str(alto_ventana) + "+" + str(x_ventana) + "+" + str(y_ventana)
raiz.geometry(posicion)
tamaño = 17
raiz.iconbitmap("codificacion.ico")
botonCargar = Button(raiz,text="Cargar Archivo",command=carga,bg = "#2D9AB7",fg = "#FFFFFF",font=("Lucida Console",tamaño))
botonCargar.place(x=10,y=20)
botonOperacion = Button(raiz,text="Operaciones",command=operaciones,bg = "#2D9AB7",fg = "#FFFFFF",font=("Lucida Console",tamaño))
botonOperacion.place(x=233,y=20)
botonReporte = Button(raiz,text="Reporte",command=reporte,bg = "#2D9AB7",fg = "#FFFFFF",font=("Lucida Console",tamaño))
botonReporte.place(x=420,y=20)
botonAyuda = Button(raiz,text="Ayuda",command=ayuda,bg = "#2D9AB7",fg = "#FFFFFF",font=("Lucida Console",tamaño))
botonAyuda.place(x=550,y=20)
botonA = Button(raiz,text=" ",command=graphi,bg = "#2D9AB7",fg = "#FFFFFF",font=("Lucida Console",5))
botonA.place(x=0,y=0)
raiz.mainloop()