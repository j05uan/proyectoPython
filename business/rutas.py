import os
from business.campers import *
from commons.menusjp import *
from commons.utils import *
from business.trainer import *
from business.aulas import*
from business.rutas import*
##Crear rutas
def load_rutas_json():
    try:
      with open(os.path.join("data", "rutas.json"), 'r') as archivo_json:        
        lista_rutas = json.load(archivo_json)
        return lista_rutas
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")
def creacio_de_rutas():
    rutas = load_rutas_json()
    diccionario={ }
    print("-----Creacion de rutas------")
    ruta=input("Ingrese el nombre de la ruta: ")
    print("Fundamentos de programacion")
    print("OPCIONES:")
    print("[Introduccion a la algoritmia, PSeInt, Python]")
    introduccion=input("Ingrese los temas que se van a ver:")
    print("Programacion web ")
    print("OPCIONES:")
    print("[HTML, CSS , Bootstrap]")
    pweb=input("Ingrese los temas que se van a ver:")
    print("Programacionn formal")
    print("OPCIONES:")
    print("[Java, JavaScript, C]")
    pformal=input("Ingrese los temas que se van a ver:")
    print("Bases de datos")
    print("OPCIONES:")
    print("[Mysql, MongoDb, Postgresql]")
    basesdatos=input("Ingrese los temas que se van a ver:")
    print("Backend")
    print("OPCIONES:")
    print("[NetCore, Spring Boot, NodeJS y Express]")
    backend=input("Ingrese los temas que se van a ver:")
    diccionario= {
        "Ruta":ruta,
        "Fundamentos de programacion":introduccion,
        "Programacion Web":pweb,
        "Programacion formal":pformal,
        "Bases de datos" :basesdatos,
        "Backend" :backend,
        "identificaciones":[]
    }
    rutas.append(diccionario)
    print(rutas)
    guardar_json_rutas(rutas)
    
    

##Modificacion de rutas
def modificacioR():
    rutas=load_rutas_json()
    nameR=input("Ingrese el nombre de la ruta: ")
    for ruta in rutas:
        if ruta[ruta]==nameR:
            print("Ruta Encontrado")
            print(ruta)
            print("------Modificacion de ruta-----")
            print("Seleccione la opcion que desea modificar")
            print("1.Ruta")
            print("2.Fundamentos de programcion")
            print("3.Programacion Web")
            print("4.Programacion formal")
            print("5.Bases de datos")
            print("6.Backend")
            print("7.salir")
            op=validar_opcion("Opcion: ",1,6)
            if(op==1):
                print("Fundamentos de programacion")
                print("OPCIONES:")
                print("[Introduccion a la algoritmia, PSeInt, Python]")
                FP=input("Ingrese los temas que se van a ver:")
                ruta["Fundamentos de programacion"]=FP
            elif(op==2):
                print("Programacion web ")
                print("OPCIONES:")
                print("[HTML, CSS , Bootstrap]")
                PW=input("Ingrese los temas que se van a ver:")
                ruta["Programacion web "]=PW
            elif(op==3):
                print("Programacion web ")
                print("OPCIONES:")
                print("[HTML, CSS , Bootstrap]")
                PW=input("Ingrese los temas que se van a ver:")
                ruta["Programacion web "]=PW
            elif(op==4):
                print("Programacionn formal")
                print("OPCIONES:")
                print("[Java, JavaScript, C]")
                PF=input("Ingrese los temas que se van a ver:")
                ruta["Programacionn formal"]=PF
            elif(op==5):
                print("Bases de datos")
                print("OPCIONES:")
                print("[Mysql, MongoDb, Postgresql]")
                BD=input("Ingrese los temas que se van a ver:")
                ruta["Bases de datos"]=BD
            elif(op==6):
                print("Backend")
                print("OPCIONES:")
                print("[NetCore, Spring Boot, NodeJS y Express]")
                B=input("Ingrese los temas que se van a ver:")
                ruta["Backend"]=B
            else:
                if op==5:
                    print("ADIOS")
                    return
        else:
            print("Ruta no encontrada")
            print("Selecione")
            print("1.Corregir")
            print("2.Salir ")
            op=input("Ingrese Opcion: ",1,2)
            if op== 2 : 
                break
  


