###Juntar, trainers, aulas, rutas, horario(mañana o tarde)
from commons.utils import *
def Crear_horario():
    aulas = load_aulas_json()
    trainers = load_trainers_json()
    horarios = load_horarios_json()
    diccionar = {}
    for aula in aulas:
        if(aula["trainer"] == ""):
            print("Seleccione uno de los siguientes trainers")
            mostrar_lista_con_diccionarios(trainers)
            i = 0
            while(True):
                try:
                    i = int(input("Seleccione el numero del trainer"))
                    break
                except Exception:
                    print("Valor invalido")
            diccionar = aula
            diccionar["trainer"] = trainers[i]["nombres"]
            aula["trainer"] = trainers[i]["nombres"]
            horarios.append(diccionar)
            break
    if(diccionar == {}):
        print("No tienen aulas disponibles")
        input("")
        return
    guardar_json_aulas(aulas)
    guardar_json_horarios(horarios)
def mostrar_horario():
    horarios = load_horarios_json()
    print("------------- mañana----------")
    cnt = 1
    for horario in horarios:
        
        for llave in horario:
            if(cnt == 1 and horario["jornada"] == "tarde"):
                print("----------- tarde --------------------")
                cnt += 1
            if(llave != "jornada"):
                print(f"{llave}: {horario[llave]}")