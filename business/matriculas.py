
import os
from campers import *
# from commons.menusjp import * 
# from commons.utils import *
from trainer import *
from aulas import*
from rutas import*
def marticular():
    campers=load_campers_json()
    horariosdisponibles=load_horarios_json()
    cuposhabiles=0
    print("------MATRICULAR----")
    camperid=input("ingrese la identificacion del camper: ")
    for camper in campers:
            if camper["Identificacion"]==camperid:
                print("Camper encontrado")
                print("El camper se encuentra en estado: ",camper,["estado"])
                if camper["estado"]=="aprobado":
                    horarios=input("Ingrese el ID del horario: ")
                    for horario in horariosdisponibles:
                        cuposhabiles=horario["cupos"]
                        while(True):
                            if cuposhabiles!=0:
                                if horario["id"]==horarios:
                                    cuposhabiles-=1
                                    print("El Camper ha sido añadido al horario",horario["id"])
                            else:
                                print("No hay cupos disponibles en este horario.")
                  

