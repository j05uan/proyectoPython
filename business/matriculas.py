
import os
from business.campers import *
# from commons.menusjp import * 
# from commons.utils import *
from business.trainer import *
from business.aulas import*
from business.rutas import*
def marticular():
    campers=load_campers_json()
    horariosdisponibles=load_horarios_json()
    cuposhabiles=1
    print("------MATRICULAR----")
    camperid=input("ingrese la identificacion del camper: ")
    for camper in campers:
            if camper["Identificacion"]==camperid:
                print("Camper encontrado")
                print("El camper se encuentra en estado: ",camper["Estado"])
                if camper["Estado"]=="aprobado":
                    horarios=input("Ingrese el ID del horario al que desea matricular: ")
                    for horario in horariosdisponibles:
                        cuposhabiles=horario["cupos"]
                        while(True):
                            if cuposhabiles!=0:
                                if horario["id"]==horarios:
                                    horario["campers"].append(camperid)
                                    cuposhabiles-=1
                                    print("El Camper ha sido añadido al horario",horario["id"])
                                    guardar_json_horarios(horarios)
                            else:
                                print("No hay cupos disponibles en este horario.")
            
                  

