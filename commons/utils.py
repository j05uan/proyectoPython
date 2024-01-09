import os
from business.campers import *
from commons.menusjp import *
from commons.utils import *
from business.trainer import *
def guardar_json_filtros(lista):
    try:
      with open(os.path.join("data", "filtro.json"), "w") as archivo_json:
        json.dump(lista, archivo_json, indent=2)
        #print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya filtros guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
def guardar_json_campers(lista):
    try:
      with open(os.path.join("data", "campers.json"), "w") as archivo_json:
        json.dump(lista, archivo_json, indent=2)
        #print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya filtros guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")

def guardar_json_filtros(lista):
    try:
      with open(os.path.join("data", "filtro.json"), "w") as archivo_json:
        json.dump(lista, archivo_json, indent=2)
        #print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya filtros guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
def guardar_json_aulas(lista):
    try:
      with open(os.path.join("data", "aulas.json"), "w") as archivo_json:
        json.dump(lista, archivo_json, indent=2)
        #print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya filtros guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
    
def guardar_json_rutas(lista):
    try:
      with open(os.path.join("data", "rutas.json"), "w") as archivo_json:
        json.dump(lista, archivo_json, indent=2)
        #print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya filtros guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
def guardar_json_matriculas(lista):
    try:
      with open(os.path.join("data", "matriculas.json"), "w") as archivo_json:
        json.dump(lista, archivo_json, indent=2)
        #print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya filtros guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
def guardar_json_treiner(lista):
    try:
      with open(os.path.join("data", "trainer.json"), "w") as archivo_json:
        json.dump(lista, archivo_json, indent=2)
        #print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya filtros guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
def guardar_json_horarios(lista):
    try:
      with open(os.path.join("data", "horarios.json"), "w") as archivo_json:
        json.dump(lista, archivo_json, indent=2)
        #print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya filtros guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")
def load_trainers_json():
    try:
      with open(os.path.join("data", "trainers.json"), 'r') as archivo_json:        
        lista = json.load(archivo_json)
        #print("La lista de trainers ha sido guardada")
        return lista
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")
def load_matriculas_json():
    try:
      with open(os.path.join("data", "trainers.json"), 'r') as archivo_json:        
        lista = json.load(archivo_json)
        #print("La lista de trainers ha sido guardada")
        return lista
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")
def load_horarios_json():
    try:
      with open(os.path.join("data", "horarios.json"), 'r') as archivo_json:        
        lista = json.load(archivo_json)
        #print("La lista de trainers ha sido guardada")
        return lista
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")
def load_campers_json():
    try:
      with open(os.path.join("data", "campers.json"), 'r') as archivo_json:        
        lista = json.load(archivo_json)
        #print("La lista de campers ha sido guardada")
        return lista
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")
def load_filtros_json():
    try:
      with open(os.path.join("data", "filtro.json"), 'r') as archivo_json:        
        lista = json.load(archivo_json)
        #print("La lista de campers ha sido guardada")
        return lista
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")
def load_aulas_json():
    try:
      with open(os.path.join("data", "aulas.json"), 'r') as archivo_json:        
        lista = json.load(archivo_json)
        #print("La lista de campers ha sido guardada")
        return lista
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")
def mostrar_lista_con_diccionarios(lista):
    for datos in lista:
        print(datos)
def limpiar_pantalla():
    os.system('clear' if os.name == 'posix' else 'cls')    


def validar_opcion(enunciando,inferior,superior):
    while True:
        try:
            opcion =int(input(enunciando))
            if opcion>=inferior and opcion<=superior:
                return opcion
            else:
                print(f"Opción no está entre el intervalo de ({inferior}-{superior})")
        except ValueError:
            print("Por favor, introduce un número válido. ")

def registro_prueba_inicial():
    campers=load_campers_json()
    campers=[]
    camper_aprobados=[]
    media =0
    texto="No inscrito"
    estado=""
    seguir=""
    while True:
        if seguir =="no":
            break
        id= ""
        while True:
            id= input("Ingrese la identificacion del camper: ")
            for camper in campers:
                if camper["Identificacion"]==id:
                    texto="El estudiente esta inscrito "
                    estado="inscrito"
                    break
                else:
                    estado="No inscrito"
                    print(" No se encontro el camper ")
                    print("Selecione")
                    print("1.Corregir")
                    print("2.Salir ")
                    op=validar_opcion("Ingrese Opcion: ",1,2)
                    if op== 2 :
                        break
            if(estado == "inscrito"):
                break
            print("El estado del camper es", estado)
            if estado =="inscrito":
                print("Ingrese los registros de la prueba inical: ")
                nota1=float(input("ingrese la nota teorica: "))
                nota2=float(input("ingrese la nota pracactica "))
                media=(nota1+nota2)/2
                if media >= 60:
                    estado= "aprobado" 
                    for camper in campers:
                            if camper["Identificacion"]==id:
                                camper["estado"]= "aprobado"
                                camper_aprobados.append(id)
                                print(camper_aprobados)
                                break
                    print("¡¡¡Felicitacioness!!!")
                    print("El camper ha sido aprobado para el curso: ")
                else:
                    estado="reprobado"
                    for camper in campers:
                        if camper["Identificacion"]==id:
                            camper["estado"] = "reprobado"
                            camper_aprobados.remove(id)
                            #rutas[0]["identificaciones"].remove(id)
                            # rutas[1]["identificaciones"].remove(id)
                            # rutas[2]["identificaciones"].remove(id)
                    print("El camper no ha sido aprobado, suerte la proxima.")

