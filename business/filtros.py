import os
from business.campers import *
from commons.menusjp import * 
from commons.utils import *
from business.trainer import *
from business.aulas import*
from business.rutas import*


def guardar_json(lista,modo):# si pasa "w" sobrescribe todo, si pasa "a" añade en lo que ya esta
    try:
      with open(os.path.join("data", "filtros.json"), modo) as archivo_json:
        json.dump(lista, archivo_json, indent=2)
        #print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya campers guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")

##Creacion de filtros
def Creacion_de_filtro():
    filtros=load_filtros_json()
    print("-----Creacion de filtro----")
    nombre=input("Ingrese el nombre del filtro: ")
    diccionario={
        "Filtro":nombre,
        "Calificaciones":[{"Identificacion":" ","nota":" "}]

    }
    filtros.append(diccionario)
    guardar_json_filtros(filtro)

def filtro():
    campers = load_campers_json()
    filtros=load_filtros_json()
    nombre_filtro = input("Ingrese el nombre del filtro")
    encontrado = False
    for filtro in filtros:
        if filtro["Filtro"] == nombre_filtro:
            encontrado = True
    if(not encontrado):
        print("No tiene filtro con ese nombre")
        return
    id=input("Ingrese la identificacion del camper: ")
    for camper in campers:
        if camper["Identificacion"]==id:
            print("Camper encontrado")
            while (True):
                print("----FILTRO----")
                nota1=input("Ingrese la nota correspondiente al 60%: " )
                nota2=input("Ingrese la nota correspondiente al 30%: " )
                nota3=input("Ingrese la nota correspondiente al 10%: ")
                nota=0
                nota=(nota1)*(0.6)+(nota2*0.3)+(nota3*0.1)
                if nota>=60:
                    print("El camper ha pasado el filtro")
                    for filtro in filtros:
                        if filtro["Filtro"] == nombre_filtro:
                            filtro["Calificaciones"].append({"Identificacion":id,"nota":nota})
                    guardar_json_filtros(filtros)
                    # diccionario={
                    #     "Filtro":nombre_filtro,
                    #     "Calificaciones":[{"Identificacion":id,"nota":nota}]
                    # }
                else:
                    print("El camper no ha sido pasado el filtro. ")
        else:
            print("El camper no ha sido encontrado")
            print("Seleccione: ")
            print("1.Corregir")
            print("2.Salir")
            op=validar_opcion("Opcion: ",1,2)
            if op==2:
                break
