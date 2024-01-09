import json
import os
from commons.utils import *
from commons.menusjp import *


def guardar_json(lista,modo):# si pasa "w" sobrescribe todo, si pasa "a" añade en lo que ya esta
    try:
      with open(os.path.join("data", "campers.json"), modo) as archivo_json:
        json.dump(lista, archivo_json, indent=2)
        #print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")



def crear_campers():
    
    print("Inscripcion de campers ")
    diccionaario ={}
    while True:
        id = input("Ingrese identificacion: ")
        apellido=input("Ingese los 2  apellidos: ")
        nombre=input("Ingrese todos los nombres: ")
        direccion=input("Ingrese direccion: ")
        acudiente=input("Ingrese el nombre completo del acudiente: ")
        celular=input("Ingrese el numero de celular: ")
        telefono=input("Ingrese numero de telefono: ")
        estado="inscrito"
        
        diccionaario = {
            "Identificacion" : id,
            "Apellido": apellido,
            "Nombre" : nombre,
            "Direccion" : direccion,
            "Acudiente" : acudiente,
            "Telefono" : telefono,
            "Celular" : celular,
            "Estado": estado
            }
        print("Ingresar informacion de otro inscrito.")
        ingreso=-1
        ingreso = int(input("Si desea agregar otro camper escriba 1, si no, escriba 0: "))
        if ingreso==0:
            break
    return diccionaario

def modificacion_campers():
   ## modificar campes
    campers=load_campers_json()
    print("---menu modificacion de camper---")
    for camper in campers:
        ingreseid=input("Ingrese la identificacion del camper: ")
        if camper["Identificacion"]==ingreseid:
            print("Camper encontrado")
            print("El camper se encuentra en estado: ",camper["estado"])
            print("-------Informacion del camper------")
            print(camper)
            print("¿Que opcion desea modificar del camper? ")
            print( "1.id")
            print("2.apellido")
            print("3.nombre")
            print("4.direccion")
            print("5.acudiente")
            print("6.celular")
            print("7.telefono")
            print("8.estado")
            print("9.Salir")
            op=validar_opcion("Opcion: ",1,9)
            # limpiar_pantalla()
            if op==1:
                new_id=input("Ingrese la modificaion: ")
                camper["Identificacion"]=new_id
                guardar_json(campers,"w")
                return
            if op==2:
                new_apellido=input("Ingrese la mmodificacion de los apellidos:")
                camper["Apellido"]=new_apellido
                guardar_json(campers,"w")
                return
            if op==3:
                new_nombre=input("Ingrese la mmodificacion de los nombres:")
                camper["Nombre"]=new_nombre
                guardar_json(campers,"w")
                return
            if op==4:
                new_direccion=input("Ingrese la mmodificacion de la direccion:")
                camper["Direccion"]=new_direccion
                guardar_json(campers,"w")
                return
            if op==5:
                new_acudiente=input("Ingrese la mmodificacion del nombre completo del acudiente:")
                camper["Acudiente"]=new_acudiente
                guardar_json(campers,"w")
                return
            if op==6:
                new_celular=input("Ingrese la mmodificacion del numero celular:")
                camper["Celular"]=new_celular
                guardar_json(campers,"w")
                return
            if op==7:
                new_telefono=input("Ingrese la mmodificacion del numero de telefono:")
                camper["Telefono"]=new_telefono
                guardar_json(campers,"w")
                return
            if op==8:
                new_estado=input("Ingrese la mmodificacion del estado:")
                camper["Estado"]=new_estado
                guardar_json(campers,"w")
                return
            if op == 9:
                print("ADIOS")
                return
        else:
            print("la idetificaion no ha sido registrada.")
            print("Desea corregir: ")
            print("1.Si")
            print("2.No")
            op=validar_opcion("Opcion: ",1,2)
            if op==2:
                break


            