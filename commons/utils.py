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
def guardar_json_registro_prueba_inicial(lista):
    try:
      with open(os.path.join("data", "registro_prueba_inicial.json"), "w") as archivo_json:
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
        print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya filtros guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")

def guardar_json_filtros(lista):
    try:
      with open(os.path.join("data", "filtros.json"), "w") as archivo_json:
        json.dump(lista, archivo_json, indent=2)
        #print("La lista de campers ha sido guardada")
    except FileNotFoundError:
        print("El archivo no existe. Puede que aún no haya filtros guardados.")
    except json.JSONDecodeError:
        print("Error al decodificar el archivo JSON . El formato podría ser incorrecto.")
    except Exception as e:
        print("Error desconocido:")

def guardar_json_camper_aprobado(lista):
    try:
      with open(os.path.join("data", "camper_aprobado.json"), "w") as archivo_json:
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
def guardar_json_trainers(lista):
    try:
      with open(os.path.join("data", "trainers.json"), "w") as archivo_json:
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

def load_camper_aprobado_json():
    try:
      with open(os.path.join("data", "camper_aprobado.json"), 'r') as archivo_json:        
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
def load_rutas_json():
    try:
      with open(os.path.join("data", "rutas.json"), 'r') as archivo_json:        
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
def load_registro_prueba_inicial_json():
    try:
      with open(os.path.join("data", "registro_prueba_inicial.json"), 'r') as archivo_json:        
        lista = json.load(archivo_json)
        #print("La lista de campers ha sido guardada")
        return lista
    except Exception as e:
      print(f"Error al guardar el archivo: {e}")
def load_filtros_json():
    try:
      with open(os.path.join("data", "filtros.json"), 'r') as archivo_json:        
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
def load_camper_aprobado_json():
    try:
      with open(os.path.join("data", "camper_aprobado.json"), 'r') as archivo_json:        
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
    camper_aprobado=load_camper_aprobado_json()
    media =0
    estado="No Inscrito"
    op=0
    notas=load_registro_prueba_inicial_json()
    while True:
        id= ""
        while True:
            id= input("Ingrese la identificacion del camper: ")
            for camper in campers:
                
                if camper["Identificacion"]==id:
                    estado="inscrito"
                    break
            if(estado == "No Inscrito"):
                 estado="No Inscrito"
                 print(" No se encontro el camper ")
                 print("Selecione")
                 print("1.Corregir")
                 print("2.Salir ")
                 op=validar_opcion("Ingrese Opcion: ",1,2)
            if op== 2 and estado=="No Inscrito" :
                 break
            print("El estado del camper es", estado)
            if estado =="inscrito":
                print("Ingrese los registros de la prueba inical: ")
                nota1=float(input("ingrese la nota teorica: "))
                nota2=float(input("ingrese la nota pracactica "))
                media=(nota1+nota2)/2
                diccionario={
                            "id": id,
                             "nota1":nota1,
                             "nota2":nota2,
                             "nota definitiva":media 
                                }
                notas.append(diccionario)
                guardar_json_registro_prueba_inicial(notas)
                if media >= 60:
                    estado= "aprobado" 
                    for camper in campers:
                            if camper["Identificacion"]==id:
                                camper["Estado"]= "aprobado"
                                camper_aprobado.append(id)
                                print(camper_aprobado)
                                break
                    print("¡¡¡Felicitacioness!!!")
                    print("El camper ha sido aprobado para el curso: ")
                    guardar_json_campers(campers)
                    guardar_json_camper_aprobado(camper_aprobado)
                    break
                else:
                    estado="reprobado"
                    for camper in campers:
                        if camper["Identificacion"]==id:
                            camper["Estado"] = "reprobado"
                            if(id in camper_aprobado):
                                camper_aprobado.remove(id)
                    print("El camper no ha sido aprobado, suerte la proxima.")
                    guardar_json_campers(campers)
                    guardar_json_camper_aprobado(camper_aprobado)
                    break
        print("¿Desea agregar las notas de otro camper?")
        print("Selecione")
        print("1.Si")
        print("2.No(Salir) ")
        op=validar_opcion("Ingrese Opcion: ",1,2)
        if op==2:
            guardar_json_campers(campers)
            guardar_json_registro_prueba_inicial(notas)
            break
                    

