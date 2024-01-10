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
                break
    elif(op == 2):
        while(True):
            op=menu_registro_prueba_inicial()
            if (op==1):
                print("-----Registro prueba inicial-----")
                registro_prueba_inicial()
            elif(op==2):
                print("ADIOS")
                break
    elif(op == 3):
        while(True):
            op=menu_trainers()
            if(op==1):
                crear_trainers()
                # guardar_json_trainer(trainers)
            elif(op==2):
                trainers = load_trainers_json()
                mostrar_lista_con_diccionarios(trainers)
                input("Oprima cualquier tecla para salir")
            elif(op==3):
                trainers=load_trainers_json()
                trainers.append(modificacion_trainers())
            elif(op == 4):
                print("ADIOS")
                break
    elif(op == 4):
        while(True):
            op=menu_aulas()
            if(op==1):
                crear_aulas()                
            elif(op==2):
                aulas = load_aulas_json()
                Buscar_aula()
                input("Oprima cualquier tecla para salir")
                
            elif(op==3):
                modificacion_aulas()
                
            elif(op==4):
                print("ADIOS")
                break
    elif (op==5):
        while(True):
            op=menu_rutas()
            if(op==1):
                limpiar_pantalla()
                creacio_de_rutas()
            elif(op==2):
                limpiar_pantalla()
                
                rutas = load_rutas_json()
                mostrar_lista_con_diccionarios(rutas)
                input("Oprima cualquier tecla para salir")
            elif(op==3):
                limpiar_pantalla()
                
                rutas = load_rutas_json()
                rutas.append(modificacioR())
                guardar_json_rutas()

            elif(op == 4):
                print("ADIOS")

                break
    elif (op==6):
        while(True):
            op=menu_horario()
            if(op==1):
                limpiar_pantalla()
                horario=load_horarios_json()
                horario.append(Crear_horario())
                guardar_json_horarios(horario)
            elif(op==2):
                limpiar_pantalla()
                horario=load_horarios_json()
                mostrar_horario()
                input("")
            elif(op == 3):
                print("ADIOS")

                break            
    elif(op == 7):
        while(True):
            op=menu_matriculas()
            if(op==1):
                marticular()
            if(op==2):   
                print("-----Matricula encontrada------")
                matriculas=load_matriculas_json
                mostrar_lista_con_diccionarios(matriculas)
            elif(op == 4):
                print("ADIOS")
                break       
    elif(op==8):
        while(True):
            op=mennun_filtros()
            if(op==1):
                Creacion_de_filtro()
                print("precione cualquier tecla para salir")
            elif(op==2):
                filtro()
            elif(op == 3):
                print("ADIOS")
                break
    elif(op==9):
        while(True):
            op=menu_reportes()
            if(op==1):
                campers=load_campers_json()
                mostrar_lista_con_diccionarios(campers)
                print("precione cualquier tecla para salir")
                
            elif(op==2):
                camper_aprobados=load_camper_aprobado_json()
                mostrar_lista_con_diccionarios(camper_aprobados)
                print("precione cualquier tecla para salir")
                
            elif(op==3):
                trainers=load_trainers_json()
                mostrar_lista_con_diccionarios(trainers)
                print("precione cualquier tecla para salir")
            elif(op==4):                
                print("ADIOS")
                break
    elif(op==10):
        print("¡¡Muchas Gracias!!")
        break
