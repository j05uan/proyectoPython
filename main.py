import os
from business.campers import *
from commons.menusjp import *
from commons.utils import *
from business.trainer import *
from business.aulas import*
from business.rutas import*
from business.trainer import*
from business.filtros import*
from business.horarios import*
from business.matriculas import*
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
                guardar_json_campers(campers)
            elif(op == 2):
                campers = load_campers_json()
                mostrar_lista_con_diccionarios(campers)
                input("Oprima cualquier tecla para salir")
            elif(op ==3):
                campers=load_campers_json()
                modificacion_campers
                campers.append(modificacion_campers())
            elif(op == 4):
                print("ADIOS")
                menu_principal()
                break
    if(op == 2):
        while(True):
            op=menu_registro_prueba_inicial()
            if (op==1):
                registro_prueba_inicial=load_camper_aprobado_json()
                registro_prueba_inicial=load_aulas_json()
                guardar_json_camper_aprobado
                camper_aprobados=load_camper_aprobado_json
                camper_aprobados.append(id)
                guardar_json_camper_aprobado()
            elif(op==2):
                print("ADIOS")
                menu_principal()
                break
    if(op == 3):
        while(True):
            op=menu_trainers()
            if(op==1):
                trainers = load_trainers_json()
                trainers.append(crear_trainers())
                guardar_json_treiner(trainers)
            elif(op==2):
                trainers = load_trainers_json()
                mostrar_lista_con_diccionarios(trainers)
                input("Oprima cualquier tecla para salir")
            elif(op==3):
                trainers=load_trainers_json()
                trainers.append(modificacion_trainers())
            elif(op == 4):
                print("ADIOS")
                menu_principal()
                break
    if(op == 4):
        while(True):
            op=menu_aulas()
            if(op==1):
                aulas = load_aulas_json()
                aulas.append(crear_aulas())
                guardar_json_aulas(aulas)
            elif(op==2):
                aulas = load_aulas_json()
                Buscar_aula()
            elif(op==3):
                aulas = load_aulas_json()
                aulas.append(modificacion_aulas())
                guardar_json_aulas(aulas)
            else:
                print("ADIOS")
                menu_principal()
                break
    if (op==5):
        while(True):
            op=menu_rutas()
            if(op==1):
                rutas = load_rutas_json()
                rutas.append(creacio_de_rutas())
                guardar_json_rutas(rutas)
            elif(op==2):
                rutas = load_rutas_json()
                mostrar_lista_con_diccionarios(rutas)
            elif(op==3):
                rutas = load_rutas_json()
                rutas.append(modificacioR())
                guardar_json_rutas()

            else:
                print("ADIOS")
                menu_principal()
                break
    if (op==6):
        while(True):
            op=menu_horario()
            if(op==1):
                horario=load_horarios_json()
                horario.append(Crear_horario())
                guardar_json_horarios(horario)
            elif(op==2):
                horario=load_horarios_json()
                mostrar_horario()
                input("")
            else:
                print("ADIOS")
                menu_principal()
                break
                

    if(op == 7):
        while(True):
            op=menu_matriculas()
            if(op==1):
                matriculas=load_matriculas_json
                matriculas.append(marticular())
                guardar_json_matriculas
            if(op==2):
                print("-----Matricula encontrada------")
                matriculas=load_matriculas_json
                mostrar_lista_con_diccionarios(matriculas)
            else:
                print("ADIOS")
                menu_principal()
                break
            
            
    if(op==8):
        while(True):
            op=mennun_filtros()
            if(op==1):
                filtros=load_filtros_json()
                filtros.append(Creacion_de_filtro())
            if(op==2):
                filtros=load_filtros_json()
                filtros.append(filtros())
            else:
                print("ADIOS")
                menu_principal()
                break
    if(op==9):
        while(True):
            op=menu_reportes()
            if(op==1):
                campers=load_campers_json
                mostrar_lista_con_diccionarios(campers)
            if(op==2):
                camper_aprobados=load_camper_aprobado_json(camper_aprobados)
                mostrar_lista_con_diccionarios(camper_aprobados)
            if(op==3):
                trainers=load_trainers_json()
                mostrar_lista_con_diccionarios(trainers)
            if(op==4):
                print("ADIOS")
                menu_principal()
                break
    else:
        break
