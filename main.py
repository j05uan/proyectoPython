import os
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

#lista de inscritos
campers =[] 
#lista de campers aprobados
camper_aprobados=[]
print("Inscripcion de campers ")

while True:
    # [1,2,3]
    # {1,2,3,2} = {1,2,3} conjunto - set([1,2,3])
    # {"nombre":"Carlos","edad":30} diccionario
    #creacion de nuevo usuario.
    id = input("Ingrese identificacion: ")
    apellido=input("Ingese los 2  apellidos: ")
    nombre=input("Ingrese todos los nombres: ")
    direccion=input("Ingrese direccion: ")
    acudiente=input("Ingrese el nombre completo del acudiente: ")
    celular=input("Ingrese el numero de celular: ")
    telefono=input("Ingrese numero de telefono: ")
    estado="inscrito"
    # id:input
    # nombre:input
    # direccion:input
    # acudiente:input
    # telefono:input
    # estado:input
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
    campers.append(diccionaario)
    print("Ingresar informacion de otro inscrito.")
    ingreso=-1
    ingreso = int(input("Si desea agregar otro camper escriba 1, si no, escriba 0: "))
    if ingreso==0:
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
## modificar campes
print("---menu modificacion de camper---")
ingreseid=input("Ingrese la identificacion del camper: ")
for camper in campers:
    if camper["Identificacion"]==id:
        print("Camper encontrado")
        print("El camper se encuentra en estado: ",camper,["estado"])
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
        limpiar_pantalla()
        if op==1:
            new_id=input("Ingrese la modificaion: ")
            camper["identificacion"]==new_id
        if op==2:
            new_nombre=input("Ingrese la mmodificacion de los apellidos:")
    else:
        print("la idetificaion no ha sido registrada.")
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
#Creacion de traines
trainers=[ ]
n_entrenadores=int(input("Ingrese la cantidad de entrenadores que hay disponibles: "))
for i in range (n_entrenadores):
    id_entrenador=input("Ingrese el ID: ")
    apellido_entrenador=input("Ingrese los apellidos del entrenador: ")
    entrenador=input("ingrese el nombre completo del entrenador"+i, ": ")
    diccionarioT={
        "id":id_entrenador,
        "apellidos":apellido_entrenador,
        "nombres":entrenador}
    trainers.append(diccionarioT)
    break
##modificacion de triners
modificaionT:input("Ingrese el ID: ")
for trainer in trainers:
    print("-----Informacion Triner-----")
    print(trainer)
     
    if trainer[id]==modificaionT:
        idT=input("ingrese la nueva id")
        trainer[id]==idT

    
##Asignacion de entrenadores a las rutas
for ruta in rutas:
    if ruta["nombre"] == ruta1 :
        ruta["entrenador"] = entrenador
        print(entrenador,"sera el entrenador de",ruta1)
    if ruta["nombre"] == ruta2 :
        ruta["entrenador"] = entrenador
        print(entrenador,"sera el entrenador de",ruta2)
    if ruta["nombre"] == ruta3 :
        ruta["entrenador"] = entrenador
        print(entrenador,"sera el entrenador de",ruta3)
print(rutas)
    
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