import json
import os
from commons.utils import *
from commons.menusjp import *
def guardar_json(lista,modo):# si pasa "w" sobrescribe todo, si pasa "a" añade en lo que ya esta
    try:
      with open(os.path.join("data", "trainers.json"), modo) as archivo_json:
        json.dump(lista, archivo_json, indent=2)
        #print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya trainers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
def load_trainers_json():
    try:
      with open(os.path.join("data", "trainers.json"), 'r') as archivo_json:        
        lista_trainers = json.load(archivo_json)
        #print("La lista de trainers ha sido guardada")
        return lista_trainers
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")
def crear_trainers():
    trainers={}
    n_entrenadores=int(input("Ingrese la cantidad de entrenadores que hay disponibles: "))
    for i in range (n_entrenadores):
        id_entrenador=input("Ingrese el ID: ")
        apellido_entrenador=input("Ingrese los apellidos del entrenador: ")
        entrenador=input("ingrese el nombre completo del entrenador"+str(i)+": ")
        diccionarioT={
            "id":id_entrenador,
            "apellidos":apellido_entrenador,
            "nombres":entrenador}
        trainers = diccionarioT
    return trainers

##modificacion de triners
def modificacion_trainers():  
    trainers=load_trainers_json()
    modificaionT:input("Ingrese el ID: ")
    for trainer in trainers:
        if trainer[id]==modificaionT:
            print("Trainer Encontrado")
            print("-----Informacion Triner-----")
            print(trainer)
            print("¿Que opcion desea modificar del trainer? ")
            print( "1.id")
            print("2.apellido")
            print("3.nombre")
            op=validar_opcion("Opcion: ",1,3)
            if op==1:
                idT=input("ingrese la nueva id")
                trainer[id]=idT
                guardar_json(trainers,"w")
                return
            if op==2:
                apT=input("Modifique el apellido: ")
                trainer["apellidos"]=apT
                guardar_json(trainers,"w")
                return
            if op==3:
                nameT=input("Modifique los nombres: ")
                trainer["nombres"]=nameT
            else:
                print("ADIOS")
                return
        else:
            print("Trainer no encontrado ")