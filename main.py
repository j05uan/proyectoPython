import os
from business.campers import *
from commons.menusjp import *
from commons.utils import *
from business.trainer import *

campers =[] 
camper_aprobados=[]
trainers=[]
while(True):
    op = menu_principal()
    if(op == 1):
        while(True):
            op = menu_campers()
            if(op == 1):
                campers = load_campers_json()
                campers.append(crear_campers())
                guardar_json(campers,"w")
            elif(op == 2):
                campers = load_campers_json()
                mostrar_lista_con_diccionarios(campers)
                input("Oprima cualquier tecla para salir")
            elif(op ==3):
                campers=load_campers_json()
                modificacion_campers()
            elif(op == 4):
                print("ADIOS")
                break
    if(op == 2):
        while(True):
            op=menu_trainers()
            if(op==1):
                trainers = load_trainers_json()
                trainers.append(crear_trainers())
                guardar_json(trainers,"w")
            elif(op==2):
                trainers = load_trainers_json()
                mostrar_lista_con_diccionarios(trainers)
                input("Oprima cualquier tecla para salir")
            elif(op==3):
                trainers=load_trainers_json()
                modificacion_trainers()
    elif(op == 6):
        break        

print(campers)
print("Prueba inicial")
#rutas
rutas=[{"nombre":"Ruta NodeJS",
        "identificaciones":[ ]}, {"nombre":"Ruta Java","identificaciones": [ ]}, {"nombre":"Ruta NetCore", "identificacioes":[ ]}]
#rgistro_de_prueba
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
                print(" El camper ", estado)
                print("Selecione")
                print("1.Corregir")
                print("2.Salir ")
                op=input("Ingrese Opcion: ")
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
                    camper["estado"] = "aprobado"
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
                    rutas[0]["identificaciones"].remove(id)
                    # rutas[1]["identificaciones"].remove(id)
                    # rutas[2]["identificaciones"].remove(id)
            print("El camper no ha sido aprobado, suerte la proxima.")            
    
    ##Asignacion de ruta, para los camper con estado aprobado 
    print(camper_aprobados)
    cupos=99

    if estado =="aprobado":
        if cupos>66:
            rutas[0]["identificaciones"].append(id)
            cupos-=1
            print("El camper pertenece a la Ruta NodeJS ")
        if cupos<66 and cupos>33:
            rutas[1]["identificaciones"].append(id)
            cupos-=1
            print("El camper pertenece a la Ruta Java ")
        if cupos<33:
            rutas[2]["identificaciones"].append(id)
            cupos-=1
            print("El camper pertenece a la Ruta NetCore ")
        
        print("¿Deseas seguir agregando notas a otro camper?")
        seguir=input("Si desea seguir escriba si, de no ser asi, escriba no:")

ruta1="Ruta NodeJS"
ruta2="Ruta Java"
ruta3="Ruta NetCore"

#area de entrenamiento 
area1="Artemis"
area2="Apolo"
area3="Sputnik"
for ruta in rutas:
    if ruta["nombre"]==ruta1:
        ruta["area"] = area1
    if ruta["nombre"]==ruta2:
        ruta["area"] = area2
    if ruta["nombre"]==ruta3:
        ruta["area"] = area3 
#creacion de rutas
Ruta_NodeJS=[{"Fundamentos de programacion": ["Introduccion a la algoritmia", "PSeInt", "Python"],
        "Programacion Web": ["HTML", "CSS" , "Bootstrap"],
        "Programacion formal": ["Java", "JavaScript", "C"], 
        "Bases de datos" : ["Mysql", "MongoDb", "Postgresql"],
        "Backend" : ["NetCore", "Spring Boot", "NodeJS y Express"]}]
Ruta_Java=[{"Fundamentos de programacion": ["Introduccion a la algoritmia", "PSeInt", "Python"],
        "Programacion Web": ["HTML", "CSS" , "Bootstrap"],
        "Programacion formal": ["Java", "JavaScript", "C"],
        "Bases de datos" : ["Mysql", "MongoDb", "Postgresql"], 
        "Backend" : ["NetCore", "Spring Boot", "NodeJS y Express"]}]
Ruta_NetCore=[{"Fundamentos de programacion": ["Introduccion a la algoritmia", "PSeInt", "Python"],
        "Programacion Web": ["HTML", "CSS" , "Bootstrap"],
        "Programacion formal": ["Java", "JavaScript", "C"], 
        "Bases de datos" : ["Mysql", "MongoDb", "Postgresql"],  
        "Backend" : ["NetCore", "Spring Boot", "NodeJS y Express"]}]
##Trainers
##modificacion de triners
modificaionT:input("Ingrese el ID: ")
for trainer in trainers:
    print("-----Informacion Triner-----")
    print(trainer)
     
    if trainer[id]==modificaionT:
        idT=input("ingrese la nueva id")
        trainer[id]==idT

    
##Asignacion de entrenadores a las rutas
# for ruta in rutas:
#     if ruta["nombre"] == ruta1 :
#         ruta["entrenador"] = entrenador
#         print(entrenador,"sera el entrenador de",ruta1)
#     if ruta["nombre"] == ruta2 :
#         ruta["entrenador"] = entrenador
#         print(entrenador,"sera el entrenador de",ruta2)
#     if ruta["nombre"] == ruta3 :
#         ruta["entrenador"] = entrenador
#         print(entrenador,"sera el entrenador de",ruta3)
# print(rutas)
    
#fecha de inicio
fecha_de_inicio=input("Ingrese la fecha de inicio: Dia/Mes/A帽o")
for ruta in rutas:
    if ruta["nombre"] == ruta1 :
        ruta["fecha de inicio"] = fecha_de_inicio
    if ruta["nombre"] == ruta2 :
        ruta["fecha de inicio"] = fecha_de_inicio
    if ruta["nombre"] == ruta2 :
        ruta["fecha de inicio"] = fecha_de_inicio

#fecha de finalizacion
fecha_de_finalizacio=input("igrese la fecha de finalizacion: Dia/Mes/A帽o")
for ruta in rutas:
    if ruta["nombre"] == ruta1 :
        ruta["fecha de finaizacion"] = fecha_de_finalizacio
    if ruta["nombre"] == ruta2 :
        ruta["fecha de finalizacion"] = fecha_de_finalizacio
    if ruta["nombre"] == ruta2 :
        ruta["fecha de finalizacion"] = fecha_de_finalizacio