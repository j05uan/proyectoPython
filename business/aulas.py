import json
import os
from commons.utils import *
from commons.menusjp import *

def guardar_json(lista,modo):# si pasa "w" sobrescribe todo, si pasa "a" añade en lo que ya esta
    try:
      with open(os.path.join("data", "aulas.json"), modo) as archivo_json:
        json.dump(lista, archivo_json, indent=2)
        #print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")

def load_aulas_json():
    try:
      with open(os.path.join("data", "aulas.json"), 'r') as archivo_json:        
        lista_aulas = json.load(archivo_json)
        return lista_aulas
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")
def crear_aulas():
    campers=load_campers_json()
    print("Creacion de aulas")
    diccionaario ={}
    while True:
        ncupos=0
        id = input("Asigne un numero para identificar el aula: ")
        nombre=input("Ingrese el nombre del aula: ")
        jornadas=input("Asigne una cantidad de jornadas: ")
        cupos=input("Ingrese los cupos disponibles del aula: ")
        for i in range (jornadas):
            jornada=input("Ingrese la jornada: ")
            time=input("Ingrese el horario: ")
            jornadas[i]=jornada         
        diccionaario = {
            "id":id,
            "nombre":nombre,
            "jornada":jornada,
            "horario":time,
            "cupos":cupos, 
            "campers":[],
            "trainer":""           
            }
        print("Crear otra aula. ")
        ncupos+=cupos
        ingreso=-1
        ingreso = int(input("Si desea crear otra aula escriba 1, si no, escriba 0: "))
        op=validar_opcion("Opcion: ",0,1)
        if ingreso==0:
            break
    return diccionaario

# Bucar aula

def Buscar_aula():
    aulas=load_aulas_json()
    print("---Aulas ---")
    nomAu=input("Ingrese el nomnre del aulas: ")
    for aula in aulas:
        if aula["nombre"]==nomAu:
            print("Aula encontrada")
            print(aula)
        else:
            print("Alula no encontrada")
            print("Selecione")
            print("1.Corregir")
            print("2.Salir ")
            op=validar_opcion("Ingrese Opcion: ",1,2)
            if op== 2 : 
                break

# MODIFICAR AULAS
def modificacion_aulas():
    aulas=load_aulas_json()
    print("---menu modificacion de aulas ---")
    nomAu=input("Ingrese el nomnre del aulas: ")
    for aula in aulas:
        if aula["nombre"]==nomAu:
            print("Aula encontrada")
            print("-------Informacion del Aula------")
            print(aula)
            print("¿Que opcion desea modificar del Aula? ")
            print( "1.id")
            print("2.nombre")
            print("3.jornada")
            print("4.horario")
            print("5.Salir")
            op=validar_opcion("Opcion: ",1,5)
            # limpiar_pantalla()
            if op==1:
                new_id=input("Ingrese la modificaion id : ")
                aula["id"]=new_id
                guardar_json_aulas(aulas)
                return
            if op==2:
                new_nombre=input("Ingrese la mmodificacion de los nombre: ")
                aula["nombre"]=new_nombre
                guardar_json_aulas(aulas)
                return
            if op==3:
                new_jornada=input("Ingrese la mmodificacion de los jornada: ")
                aula["jornada"]=new_jornada
                guardar_json_aulas(aulas)
                return
            if op==4:
                new_horario=input("Ingrese la mmodificacion de la horario: ")
                aula["Direccion"]=new_horario
                guardar_json_aulas(aulas)
                return
            if op==5:
                print("ADIOS")
                return
    print("Aula no encontrada.")